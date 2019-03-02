using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Enemy-Patrol-Movement
// GOAL: Moving enemy patrol units accross sandbox through negative 
// z axis units
public class EnemyPatrolMovement : MonoBehaviour  {
    // Variables for Enemy-Patrol-Movement
    public Rigidbody Patrol1;
    public Rigidbody Patrol2;
    public float speed;
    // Patrol has force added to it in order to create movement
    void Update() {
        Patrol1.AddForce(0, 0, -speed * Time.deltaTime);
        // Updates console log of curent game status 
        Debug.Log("PLASMA BEAM IS MOVING");
    }
    // Destroys patrol1 while activly moving patrol2
    // If patrol1 is destroyed, start movement for patrol2
    void OnTriggerEnter(Collider other) {
        if(other.CompareTag("Projectile")) {
            Destroy(Patrol1, 0.1f);
            Patrol2.AddForce(0,0, speed * Time.deltaTime);
        }
    }
}
// END Enemy-Patrol-Movement...