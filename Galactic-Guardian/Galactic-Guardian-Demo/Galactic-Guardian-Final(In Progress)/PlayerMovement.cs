using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour {
    public Rigidbody rb;
    public float speed;
    public Vector3 point;
    void Update() {
        Debug.Log("STARTING MOVEMENT IN XYZ AXES");
        if (Input.GetKey(KeyCode.A)) {
            transform.RotateAround(point, Vector3.up, 2 * Time.deltaTime);
            Debug.Log("PLAYER IS MOVING LEFT");
        } 
        else if (Input.GetKey(KeyCode.S)) {
            transform.RotateAround(point, -Vector3.up, 2 * Time.deltaTime);
            Debug.Log("PLAYER IS MOVING RIGHT");
        }
    }
}
