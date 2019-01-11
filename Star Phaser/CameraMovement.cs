using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour {
    public Rigidbody Player;
    public Vector3 offset;
// <!-- ==== START CAMERA MOVEMENT WITH PLAYER ==== -->
    void Movement() {
        transform.position = Player.position + offset;
    }
// <-- END CAMERA MOVEMENT WITH PLAYER -->


}
