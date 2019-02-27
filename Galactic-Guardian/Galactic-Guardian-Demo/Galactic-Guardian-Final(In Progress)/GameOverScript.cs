using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameOverScript : MonoBehaviour {
    // Update is called once per frame
    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Patrol1")) {
            Debug.Log("GAME OVER");
            Restart();
        }
    }
    void Restart() {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
