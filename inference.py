import os
from openai import OpenAI
from env import SmartClassroomEnv

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

# Fix HF_TOKEN crash
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")


client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def choose_action(state):

    prompt = f"Choose an action (0,1,2,3) to optimize classroom energy. State: {state}"

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    action = response.choices[0].message.content.strip()

    try:
        action = int(action)
    except:
        action = 3

    return action


def run_episode():

    env = SmartClassroomEnv()

    state, _ = env.reset()

    print(f"[START] task=smart-energy env=classroom model={MODEL_NAME}")

    step = 0
    rewards = []
    success = False

    try:

        done = False

        while not done and step < 20:

            action = choose_action(state)

            state, reward, done, truncated, info = env.step(action)

            step += 1
            rewards.append(reward)

            error = info.get("error", None)

            if error is None:
                error = "null"

            print(
                f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error}"
            )

        success = done

    except Exception as e:

        print(f"Error: {e}")

    finally:

        env.close()

        reward_str = ",".join([f"{r:.2f}" for r in rewards])

        print(
            f"[END] success={str(success).lower()} steps={step} rewards={reward_str}"
        )


if __name__ == "__main__":
    run_episode()