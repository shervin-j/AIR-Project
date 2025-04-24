import pybullet as p
import time
import pybullet_data

# Connect to PyBullet
p.connect(p.GUI)  # GUI mode for visualizing
p.setGravity(0, 0, -9.81)

# Set the path to PyBullet's default data for loading URDFs
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load a plane (this prevents the robot from falling off)
plane_id = p.loadURDF("plane.urdf")

# Load the Panda arm URDF (ensure you have the URDF file)
panda_arm_urdf = "franka_panda/panda.urdf"
panda_id = p.loadURDF(panda_arm_urdf, basePosition=[0, 0, 0.5])  # Place the robot slightly above the floor

# Get the number of joints in the Panda arm
num_joints = p.getNumJoints(panda_id)
print(f"Number of joints in the Panda arm: {num_joints}")

# Set initial joint positions (ensure this list matches the number of joints)
initial_joint_positions = [0] * num_joints  # Set all joints to 0 initially

# Set the joints to the initial position
for i in range(num_joints):
    p.resetJointState(panda_id, i, initial_joint_positions[i])

# Control the arm (you can change the joint positions here)
target_joint_positions = [0.5, -0.5, 0.5, -1.5, 0.5, 1.5, 0.5]

# Move the Panda arm to the target joint positions smoothly
while True:
    for i in range(num_joints):
        # Make sure target_joint_positions has at least the same number of values as num_joints
        target_pos = target_joint_positions[i] if i < len(target_joint_positions) else 0
        p.setJointMotorControl2(
            panda_id, i, p.POSITION_CONTROL, targetPosition=target_pos, force=500
        )
    
    # Step the simulation forward
    p.stepSimulation()
    
    # Sleep to control the simulation speed
    time.sleep(0.01)

    # Check if the user closes the window or presses 'q' to exit
    if p.isConnected() == 0:  # Exit the loop if the GUI window is closed
        break

# Disconnect when done
p.disconnect()
