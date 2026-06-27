import mujoco
import numpy as np

print(f"MuJoCo version: {mujoco.__version__}")

# use a built in simple model instead of a file
xml = """
<mujoco>
  <worldbody>
    <body name="box" pos="0 0 1">
      <geom type="box" size="0.1 0.1 0.1"/>
      <joint type="free"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

mujoco.mj_step(model, data)
print(f"Simulation stepped successfully")
print(f"Box position: {data.qpos}")
print("Done")