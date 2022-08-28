# Docker with Webcam
The purpose of this repository is to represent How webcam,docker and opencv-python work together [main.py](./python/main.py).

I do it for a project I am working on it to show how to use docker to run a camera for different purposes.


## Windows

#### xming
- Download the latest version of `xming` from [here](https://sourceforge.net/projects/xming/).
    - next run xLunch and follow the instructions to set settings and be sure select `no access control`
#### ffmpeg
- Download `ffmpeg` and add to my system `Path`, and then i run the following command to stream the camera:

    - How add to Path:
        - There is a lot web explanation about how to add to path on windows, but i will just use the following [link](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html).

    Next, Open cmd and run this command to lsit all device 

    ```
    ffmpeg -list_devices true -f dshow -i dummy
    ```
    will show smilie face camera and webcam

    ```
    libpostproc    56.  7.100 / 56.  7.100
    [dshow @ 0000016d4e9328c0] "c922 Pro Stream Webcam" (video)
    [dshow @ 0000016d4e9328c0]   Alternative name "@device_pnp_\\?\usb#vid_046d&pid_085c&mi_00#8&53f1919&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global"
    [dshow @ 0000016d4e9328c0] "OBS Virtual Camera" (video)
    [dshow @ 0000016d4e9328c0]   Alternative name "@device_sw_{860BB310-5D01-11D0-BD3B-00A0C911CE86}\{A3FCE0F5-3493-419F-958A-ABA1250EC20B}"
    [dshow @ 0000016d4e9328c0] "Microphone (Bose PC Desktop Controller)" (audio)
    [dshow @ 0000016d4e9328c0]   Alternative name "@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{A46D01C1-0A9E-4489-B4C7-F8A85AB5A8C5}"
    [dshow @ 0000016d4e9328c0] "Microphone (C922 Pro Stream Webcam)" (audio)
    [dshow @ 0000016d4e9328c0]   Alternative name "@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{91193E78-B4C3-4A6C-A976-7FABEE5AB09D}"

    ```

    Select the camera you want to use and run the following command to stream the camera:

    ```
    ffmpeg -f dshow -framerate 30 -i video="c922 Pro Stream Webcam" -vcodec mpeg4 -q 12 -f mpegts udp://127.0.0.1:1235
    ```

    - The `udp://<localhotsIp>:<port>` is the address where the camera will be streaming.
    - The `-q 12` is the quality of the stream.
    - The `-f mpegts` is the format of the stream.
    - The `-vcodec mpeg4` is the video codec.
    - The `-f dshow` is the format of the input.    
    - The `-i video="c922 Pro Stream Webcam"` is the input.
    - The `-framerate 30` is the framerate of the stream.

Now You start to stream your cam through your network, and you want to access it from your docker container.

Now Move to step [Docker Container Configuration](#docker-container-configuration)

## linux
- [ ] TO DO 🚧


## MAC.
> you need usb cam bulit-in cam not supported!--> 😡
- install `ffmpeg` using `brew`:
    - `brew install ffmpeg`
- install xquartz:
    - `brew cask install xquartz`
- list cam device
    ```
    ffmpeg -list_devices true -f avfoundation -i dummy
    ```
- Stream cam
    ```shell
    ffmpeg -f avfoundation -framerate 10  -i "<Camera name>"  -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f mpegts udp://127.0.0.1:<port>
    ```

## <a name="docker-container-configuration"></a> Docker Container Configuration

Add parameter to the command to stream the camera:

- with devContainer `vscode`
    ```json
    {
        "runArgs": [
            "-ti",
            "-p",
            "1235:1235/udp",
            "-e",
            "DISPLAY=<localhostIp>:0.0"
        ],
    }
    ```
- `Or` when run docker container from cmd
    
    ```shell
    docker run -ti -p 1235:1235/udp -e DISPLAY=<localhostIP>:0.0 vscode
    ```

- Docker parameter:
    - ti: to run in the background
    - p: to specify the port
    - e: to specify the environment variable
    - DISPLAY: to specify the display `ip:port` this one you will be your Ip on network you are work on.
 
 - Make sure you insall all this librarys , check [Docker](.devcontainer/Dockerfile) file:
 
 ```
     gcc g++ \
    libavcodec-dev \
    libswscale-dev \
    libavformat-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer1.0-dev \
    libpng-dev \
    libopencv-dev \
    libjpeg-dev \
    libopenexr-dev \
    libtiff-dev \
    libwebp-dev \
    wget \
    qtbase5-dev \
    qtchooser \
    qt5-qmake \
    qtbase5-dev-tools \
    libtbb-dev \
    libgphoto2-dev \
    ffmpeg \
    usbutils \
```


