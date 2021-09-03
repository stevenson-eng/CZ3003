using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AuthenticationScript : MonoBehaviour
{
    public InputField playerName;
    public InputField email;
    public InputField password;
    public InputField confirmPassword;

    void Start()
    {
        GameObject.FindGameObjectWithTag("MusicController").GetComponent<MusicScript>().PlayMusic();
    }

    public void onLoginButtonClick()
    {
        login();
    }

    public void onRegisterButtonClick()
    {
        register();
    }

    private void login()
    {
        if (email.text != "admin" || password.text != "password")
        {
            Debug.LogWarning("Wrong username/password");
        }
        else
        {
            Debug.Log("Success!");
        }
    }

    private void register()
    {
        if (!checkFieldAllFilledIn())
        {
            Debug.LogWarning("Fill in all fields!");
            return;
        }

        if (!checkPasswordAndConfirmPassword())
        {
            Debug.LogWarning("Password and Confirm Password not matching...");
            return;
        }

        Debug.Log("Success!");
    }

    private bool checkPasswordAndConfirmPassword()
    {
        return confirmPassword.text == password.text;
    }

    private bool checkFieldAllFilledIn()
    {
        return
            email.text != null && email.text != "" &&
            playerName.text != null && playerName.text != "" &&
            password.text != null && password.text != "";
    }
}
