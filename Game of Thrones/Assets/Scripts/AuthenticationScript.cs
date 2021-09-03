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
    public Canvas canvas;

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
            GameObject popup = Instantiate(Resources.Load("ErrorPopUp") as GameObject);
            PopUpScript extractPopUp = popup.GetComponent<PopUpScript>();


            if (extractPopUp != null) extractPopUp.Init(canvas, "Wrong username/password");
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
