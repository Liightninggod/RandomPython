import pyautogui
script = "Well if you wanted honesty That's all you had to say I never want to let you down or have you go It's better off this way For all the dirty looks For photographs your boyfriend took Remember when you broke your foot From jumping out the second floor? I'm not okay I'm not okay I'm not okay You wear me out What will it take to show you That it's not the life it seems? I told you time and time again You sing the words But don't know what it means To be a joke and look Another line without a hook I held you close as we both shook For the last time Take a good hard look I'm not okay I'm not okay I'm not okay You wear me out Forget about the dirty looks The photographs your boyfriend took You said you read me like a book But the pages all are torn and frayed I'm okay I'm okay I'm okay, now (I'm okay, now) But you really need to listen to me Because I'm telling you the truth I mean this I'm okay (trust me)  I'm not okay I'm not okay Well, I'm not okay I'm not o-fucking-kay I'm not okay I'm not okay (kay)"
for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")

