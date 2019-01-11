using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class TriggerRestart : MonoBehaviour
{

    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Player")){
            Debug.Log("GAME OVER");
            Restart();
        }
    }

    void Restart() {
      SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
