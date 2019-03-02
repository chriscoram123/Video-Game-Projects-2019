using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour {

    public Rigidbody rb;
    public float speed;
    void Movement() {
        Debug.Log("STARTING MOVEMENT IN XYZ AXES");   
        if (Input.GetKey("A"))  {
            rb.AddForce(200 * Time.deltaTime, 0, 45);
            Debug.Log("PLAYER IS MOVING RIGHT");
        }
        if (Input.GetKey("S")) {
            rb.AddForce(-200 * Time.deltaTime, 0, 45);
            Debug.Log("PLAYER IS MOVING LEFT");
        }
    }
}
