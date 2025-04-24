import mujoco
import mujoco.viewer  # pip install glfw or pip install mujoco[glfw]

# Path to the XML file you just cloned
xml_path = "mujoco_menagerie/franka_fr3/scene.xml"

model = mujoco.MjModel.from_xml_path(xml_path)
data  = mujoco.MjData(model)

# quick interactive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
