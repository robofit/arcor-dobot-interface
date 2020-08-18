from art_brain import ArtBrainRobotInterface, ArtGripper


class ArtDobotInterface(ArtBrainRobotInterface):

    DOBOT_ARM = "arm"

    def __init__(self, robot_helper):
        super(ArtDobotInterface, self).__init__(robot_helper)

        #self._arms.append(ArtGripper(self.DOBOT_ARM, "Dobot arm", True, False, "/art/dobot/pp_client", None,
        #                             None, None,
        #                             "/art/dobot/get_ready", None))

    def select_arm_for_pick(self, obj_id, objects_frame_id, tf_listener):
        return self.DOBOT_ARM

    def select_arm_for_pick_from_feeder(self, pick_pose, tf_listener):
        return self.DOBOT_ARM

    def select_arm_for_drill(self, obj_to_drill, tf_listener):
        return self.DOBOT_ARM

    def prepare_for_calibration(self):
        pass

    def emergency_stop(self):
        pass

    def restore_robot(self):
        pass

