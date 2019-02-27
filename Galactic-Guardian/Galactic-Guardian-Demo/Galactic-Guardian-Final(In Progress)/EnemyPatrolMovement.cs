using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//Script for moving enemy patrol units accross sandbox
public class EnemyPatrolMovement : MonoBehaviour  {
    public Rigidbody Patrol1;
    public Rigidbody Patrol2;
    public float speed;
    // Update is called once per frame
    // Update adds force to patrol 1
    void Update() {
        Patrol1.AddForce(0, 0, speed * Time.deltaTime);
    }
    // Destroys patrol1 while activly moving patrol2
    void OnTriggerEnter(Collider other) {
        if(other.CompareTag("Projectile")) {
            Destroy(Patrol1, 0.1f);
            Patrol2.AddForce(0,0, speed * Time.deltaTime);
        }
    }
}
