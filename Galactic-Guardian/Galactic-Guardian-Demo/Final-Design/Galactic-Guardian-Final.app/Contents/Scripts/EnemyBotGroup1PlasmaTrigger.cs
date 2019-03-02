using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Enemy-bot-group-1-plasma-trigger
// GOAL: When game objet comes in contact with trigger, game object
// instantiates prefab object with added force / direction
public class EnemyBotGroup1PlasmaTrigger : MonoBehaviour {
    // Variables for Enemy-bot-group-1-plasma-trigger
    public Rigidbody PlasmaBeam;
    public Transform barrelEnd;
    public float speed;
    // If object collides with trigger assigned tag EnemyPlasmaTrigger, object
    // stored in prefab will instantiate
    void OnTiggerEnter(Collider other) {
        if(other.CompareTag("EnemyPlasmaTrigger")) {
           // object is instantiated with force / direction
           Instantiate(PlasmaBeam, barrelEnd.position, barrelEnd.rotation);
            PlasmaBeam.AddForce(barrelEnd.forward * -speed);
            Update();
        }
    }

    // Update is called once per frame
    void Update() {
        // Updates console log of curent game status 
        Debug.Log("PLASMA BEAM IS MOVING");
    }
}
// END Enemy-bot-group-1-plasma-trigger...
