using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
// START...Game-Over-Script
// GOAL: End current game functions and restart game
public class GameOver : MonoBehaviour {
    // if object collides with trigger assigned tag Patrol1,
    // activate Restart() void
    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Patrol1")) {
            // Updates console log of curent game status 
            Debug.Log("GAME OVER");
            Restart();
        }
    }
    void Restart() {
        // Scene manager restarts video game 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
// END Game-Over-Script...