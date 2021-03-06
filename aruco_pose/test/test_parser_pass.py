#!/usr/bin/env python
import sys
import unittest
import json
import rospy
import rostest

from geometry_msgs.msg import PoseWithCovarianceStamped
from sensor_msgs.msg import Image
from aruco_pose.msg import MarkerArray
from visualization_msgs.msg import MarkerArray as VisMarkerArray


class TestArucoMapPass(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_parser_pass', anonymous=True)

    def test_markers(self):
        markers = rospy.wait_for_message('aruco_map/visualization', VisMarkerArray, timeout=5)
        
        self.assertEqual(len(markers.markers), 6)
# FIXME: visual marker id is not ArUco marker id
#        self.assertEqual(markers.markers[0].id, 1)
#        self.assertEqual(markers.markers[1].id, 2)
#        self.assertEqual(markers.markers[2].id, 3)
#        self.assertEqual(markers.markers[3].id, 4)

        self.assertAlmostEqual(markers.markers[0].pose.position.x, 0, places=7)
        self.assertAlmostEqual(markers.markers[0].pose.position.y, 0, places=7)
        self.assertAlmostEqual(markers.markers[0].pose.position.z, 0, places=7)
        
        self.assertAlmostEqual(markers.markers[1].pose.position.x, 1, places=7)
        self.assertAlmostEqual(markers.markers[1].pose.position.y, 1, places=7)
        self.assertAlmostEqual(markers.markers[1].pose.position.z, 1, places=7)
        
        self.assertAlmostEqual(markers.markers[2].pose.position.x, 1, places=7)
        self.assertAlmostEqual(markers.markers[2].pose.position.y, 0, places=7)
        self.assertAlmostEqual(markers.markers[2].pose.position.z, 0.5, places=7)
        
        self.assertAlmostEqual(markers.markers[3].pose.position.x, 0, places=7)
        self.assertAlmostEqual(markers.markers[3].pose.position.y, 1, places=7)
        self.assertAlmostEqual(markers.markers[3].pose.position.z, 0, places=7)
        
        self.assertAlmostEqual(markers.markers[4].pose.position.x, 1, places=7)
        self.assertAlmostEqual(markers.markers[4].pose.position.y, 0.5, places=7)
        self.assertAlmostEqual(markers.markers[4].pose.position.z, 0, places=7)
        
        self.assertAlmostEqual(markers.markers[5].pose.position.x, 2.2, places=7)
        self.assertAlmostEqual(markers.markers[5].pose.position.y, 0.2, places=7)
        self.assertAlmostEqual(markers.markers[5].pose.position.z, 0, places=7)

        self.assertAlmostEqual(markers.markers[0].scale.x, 0.33, places=7)
        self.assertAlmostEqual(markers.markers[0].scale.y, 0.33, places=7)
        self.assertAlmostEqual(markers.markers[1].scale.x, 0.225, places=7)
        self.assertAlmostEqual(markers.markers[1].scale.y, 0.225, places=7)
        self.assertAlmostEqual(markers.markers[2].scale.x, 0.45, places=7)
        self.assertAlmostEqual(markers.markers[2].scale.y, 0.45, places=7)
        self.assertAlmostEqual(markers.markers[3].scale.x, 0.15, places=7)
        self.assertAlmostEqual(markers.markers[3].scale.y, 0.15, places=7)
        self.assertAlmostEqual(markers.markers[4].scale.x, 0.25, places=7)
        self.assertAlmostEqual(markers.markers[4].scale.y, 0.25, places=7)
        self.assertAlmostEqual(markers.markers[5].scale.x, 0.35, places=7)
        self.assertAlmostEqual(markers.markers[5].scale.y, 0.35, places=7)

    def test_map_image(self):
        img = rospy.wait_for_message('aruco_map/image', Image, timeout=5)
        self.assertEqual(img.width, 2000)
        self.assertEqual(img.height, 2000)
        self.assertEqual(img.encoding, 'mono8')

    # def test_transforms(self):
    #     pass


rostest.rosrun('aruco_pose', 'test_aruco_map', TestArucoMapPass, sys.argv)
