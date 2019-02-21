using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START TURRET ROTATION PROGRAM...
// On command turret will rotate for player to align crosshair with enemy objects
//________________________________________________________________________________
public class MainTurretRotation : MonoBehaviour {

    public Rigidbody Rb;
    public float speed;

    // <!-- ==== START PLAYER MOVEMENT ==== -->
    // Player Movement On X,Y,Z Axis
    void Update()
    {
        Debug.Log("STARTING ANGULAR ROTATION IN XYZ AXES");
        if (Input.GetKey(KeyCode.LeftArrow)) {
            Rb.transform.Rotate(Vector3.left * speed * Time.deltaTime, 0, 0);
            Debug.Log("PLAYER IS MOVING RIGHT");
        }
        if (Input.GetKey(KeyCode.RightArrow)) {
            Rb.transform.Rotate(-Vector3.right * speed * Time.deltaTime, 0, 0);
            Debug.Log("PLAYER IS MOVING LEFT");
        }
    }
    // <-- END PLAYER MOVEMENT -->
}
// END TURRET ROTATION PROGRAM... :]
