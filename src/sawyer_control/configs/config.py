import sawyer_control.configs.calibration_config as calibration_config
import sawyer_control.configs.ashvin_config as ashvin_config
import sawyer_control.configs.austri_config as austri_config
import sawyer_control.configs.base_config as base_config
import sawyer_control.configs.ros_config as ros_config
config_dict = dict(
    ros_config=ros_config,
    base_config=base_config,
    austri_config=austri_config,
    calibration_config=calibration_config,
    ashvin_config=ashvin_config,
)