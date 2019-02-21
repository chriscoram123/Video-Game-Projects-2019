using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlasmaBeamDestroy : MonoBehaviour
{
    // Start is called before the first frame update
    void Start() {
        Destroy(gameObject, 1.4f);
        Update();
    }
    // Update is called once per frame
    void Update() {
        Debug.Log("BEAMS HAVE BEEN DESTROYED");
    }
}
