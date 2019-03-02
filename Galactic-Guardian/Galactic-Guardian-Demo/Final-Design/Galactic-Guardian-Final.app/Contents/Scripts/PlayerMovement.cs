using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Pl-Movement
// GOAL: On key commands move player up positive and negative
// y-axis. Also, create movement using mouse pad
public class PlMovement : MonoBehaviour {
    // Variables for MonoBehaviour
    public Rigidbody rb;
    public float speed;
    public Vector3 point;
    // Mouse / Key Inputs
    void Update() {
        float mouseInput = Input.GetAxis("Mouse X");
        Vector3 lookhere = new Vector3(0, mouseInput, 0);
        transform.Rotate(lookhere);
     
        if (Input.GetKey(KeyCode.UpArrow)) {
            transform.position += Vector3.up * speed * Time.deltaTime;
            Debug.Log("MOVE UP");
        }
        else if (Input.GetKey(KeyCode.DownArrow)) {
            transform.position += Vector3.down * speed * Time.deltaTime;
            Debug.Log("MOVE DOWN");
        }

         // Updates console log of curent game status 
        Debug.Log("PLAYER IS MOVING");
    }
}
// END PlMovement...
