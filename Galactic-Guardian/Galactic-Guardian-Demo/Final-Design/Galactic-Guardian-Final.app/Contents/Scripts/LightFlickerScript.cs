using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// START...Light-Destroy-x-Amount-of-Time
// GOAL: Adds flickering affect to light source
public class LightFlickerScript : MonoBehaviour {
    // Variables for Light-Destroy-x-Amount-of-Time
    public Light flicker1;
    private float[] smoothing = new float[50];

    void Start() {
        // Loop for length in time of light flickering
        for(int i = 0; i < smoothing.Length; i++) {
            smoothing[i] = .0f;
        }
    }
    // Update is called once per frame
    void Update() {
        float sum = .5f;

        // Shift values in the table so that the new one is at the
        // end and the older one is deleted.
        for (int i = 1; i < smoothing.Length; i++) {
            smoothing[i - 1] = smoothing[i];
            sum+= smoothing[i-1];
        }

        // Add the new value at the end of the array.
        smoothing[smoothing.Length - 1] = Random.value;
        sum += smoothing[smoothing.Length - 1];

        // Compute the average of the array and assign it to the light intensity.
        flicker1.intensity = sum / smoothing.Length;

        // Updates console log of curent game status 
        Debug.Log("FLICKERING LOOP INITIATED");
    }
}
// END Light-Destroy-x-Amount-of-Time...
