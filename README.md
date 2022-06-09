# Notecard Random Example using the Notecard Balena Block

This is an example of how to use the balena [Block](https://www.balena.io/blog/balenablocks-public-roadmap/) for interfacing with the [Blues Wireless Notecard](https://blues.io/products/notecard/).

Add this block to your Balena fleet to easily send data to your cloud backend via the Notecard using low-power cellular connection.

## Deploy the Random example

On this example we will use the Notecard block and another container that will generate random numbers. The `random` container will send the random numbers to the Notehub using the Blues Wireless connectivity.


### Hardware and Software

The hardware needed to run this example project are:

* Raspberry Pi 4.
* [Notecard Raspberry Pi Kit](https://shop.blues.io/products/raspberry-pi-starter-kit). 
* [Notecard](https://shop.blues.io/products/note-nbgl-500)

* A free [balenaCloud account](https://dashboard.balena-cloud.com/)
* Create a [Notehub](https://notehub.io/) account.


### Via [Balena Deploy](https://www.balena.io/docs/learn/deploy/deploy-with-balena-button/)

Running this project is as simple as deploying it to a balenaCloud application. You can do it in just one click by using the button below:

[![](https://www.balena.io/deploy.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/mpous/notecard-random)

Follow instructions, click Add a Device and flash an SD card with that OS image dowloaded from balenaCloud. Enjoy the magic 🌟Over-The-Air🌟!

#### Via [Balena-Cli](https://www.balena.io/docs/reference/balena-cli/)

If you are a balena CLI expert, feel free to use balena CLI.

- Sign up on [balena.io](https://dashboard.balena.io/signup)
- Create a new application on balenaCloud.
- Clone this repository to your local workspace.
- Using [Balena CLI](https://www.balena.io/docs/reference/cli/), push the code with `balena push <application-name>`
- See the magic happening, your device is getting updated 🌟Over-The-Air🌟!

### Configure the Variables

You will need to define the Device Variables `productID` and `fileID` to define where to send the data to the Notehub. 

Once you create an account at the NoteHub, create a new project and you will get the `productID` of your project. The `fileID` might be related with your notefile. Read more [here](https://dev.blues.io/notecard/notecard-walkthrough/inbound-requests-and-shared-data/) to understand the `fileID`component.

