let rps = 0
let angle = 0
let count = 0
let player = 0
radio.setGroup(1)
player = 0
while (true) {
    count = 3
    angle = 90
    pins.servoWritePin(AnalogPin.P0, angle)
    basic.showString("Ready", 50)
for (let i = 0; i < 3; i++) {
        music.playTone(165, music.beat(BeatFraction.Whole))
        basic.showNumber(count)
        basic.pause(1000)
        count = count - 1
    }
    music.playTone(880, music.beat(BeatFraction.Whole))
    basic.showIcon(IconNames.Yes)
    // basic.showString("GO", 25)
    rps = Math.random(3)
    if (rps == 0) {
        angle = 0
        pins.servoWritePin(AnalogPin.P0, angle)
        basic.showIcon(IconNames.Diamond)
    } else {
        if (rps == 1) {
            angle = 180
            pins.servoWritePin(AnalogPin.P0, angle)
            basic.showIcon(IconNames.Square)
        } else {
            angle = 270
            pins.servoWritePin(AnalogPin.P0, angle)
            basic.showIcon(IconNames.Scissors)
        }
    }
    basic.pause(3000)
}
