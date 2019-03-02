using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Projectile-Movement
// GOAL: Instantiate and add forxe to rojectile from Input
public class ProjectileMovement : MonoBehaviour {
    // Variables for Projectile-Movement
    public Rigidbody Projectiles;
    public Transform barrelEnd;
    public float speed;
    // Update is called once per frame
    // if user hits "e", projectile should instantiate
    void Update() {
        // if statement for instantiate / add force
        if (Input.GetKey("e")) {
            Instantiate(Projectiles, barrelEnd.position, barrelEnd.rotation);
            Projectiles.AddForce(500 * speed * Time.deltaTime, 0, 0);
            // Updates console log of curent game status 
            Debug.Log("PROJECTILE HAS BEEN INSTANTIATED");
        }
    }
}
// END Projectile-Movement...