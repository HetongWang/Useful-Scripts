#include <windows.h>
#include <stdio.h>
#include<iostream>
using namespace std;
main()
{
    //get the resolution
    int Width = GetSystemMetrics(SM_CXSCREEN);
    int Height = GetSystemMetrics(SM_CYSCREEN);

    DEVMODE lpDevMode0;
    lpDevMode0.dmBitsPerPel=32;
    lpDevMode0.dmPelsWidth=1280;
    lpDevMode0.dmPelsHeight=720;
    lpDevMode0.dmSize=sizeof(lpDevMode0);
    lpDevMode0.dmFields =DM_PELSWIDTH|DM_PELSHEIGHT|DM_BITSPERPEL;
    //modified the resolution
    DEVMODE lpDevMode;
    lpDevMode.dmBitsPerPel=32;
    lpDevMode.dmPelsWidth=1920;
    lpDevMode.dmPelsHeight=1080;
    lpDevMode.dmSize=sizeof(lpDevMode);
    lpDevMode.dmFields =DM_PELSWIDTH|DM_PELSHEIGHT|DM_BITSPERPEL;
    if (Width == 1280)
        ChangeDisplaySettings(&lpDevMode,0);
    else
        ChangeDisplaySettings(&lpDevMode0,0);

}
