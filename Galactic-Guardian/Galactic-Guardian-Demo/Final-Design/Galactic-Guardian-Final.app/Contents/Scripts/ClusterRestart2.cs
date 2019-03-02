using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Cluster Restart 2
// GOALS: Provide cluster restart 2with ontriggers that will restart 
// game object to original position
public class ClusterRestart2 : MonoBehaviour {
    // Variables for cluster restart 2
    public Rigidbody enemy;
    Vector3 initialPos;
    
    // OnTriggerEnter will restart object to original position when in contact with box
    // collider trigger "Restart2"
    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Restart2")) {
             // Restart at original x,y,z coordinates
            enemy.transform.position = initialPos;
            Update();
        }
    }
    // Update is called once per frame
    void Update() {
     // Updates console log of curent game status 
     Debug.Log("CLUSTER HAS RESTARTED POSITION");
    }
}
// END CLUSTER RESTART...