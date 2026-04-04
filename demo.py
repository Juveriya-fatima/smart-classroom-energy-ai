from env import SmartClassroomEnv

env = SmartClassroomEnv()

state, _ = env.reset()

print("SMART CLASSROOM ENERGY AI DEMO")
print("--------------------------------")

students, temperature, lights, ac, computers, time_of_day = state

time_names = ["Morning", "Afternoon", "Evening"]

print("Initial Classroom State:")
print("Students:", int(students))
print("Temperature:", int(temperature))
print("Time:", time_names[int(time_of_day)])
print("Lights:", "ON" if lights else "OFF")
print("AC:", "ON" if ac else "OFF")
print("Computers:", "ON" if computers else "OFF")

print("\nAI making decisions...\n")

for step in range(10):

    action = env.action_space.sample()

    state, reward, done, _, _ = env.step(action)

    students, temperature, lights, ac, computers, time_of_day = state

    print("Step", step + 1)
    print("Students:", int(students))
    print("Temperature:", int(temperature))
    print("Time:", time_names[int(time_of_day)])
    print("Lights:", "ON" if lights else "OFF")
    print("AC:", "ON" if ac else "OFF")
    print("Computers:", "ON" if computers else "OFF")
    print("Reward:", reward)
    print("--------------------------")