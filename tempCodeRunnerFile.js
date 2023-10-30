function printReversedStarLadder(steps) {
    for (let i = steps; i >= 1; i--) {
        let row = '';
        // console.log(row);
        
        for (let j = 1; j <= i; j++) {
            row += '*';
        }
        console.log(row);
    }
}

const steps = 5; // You can change this value to adjust the ladder height

printReversedStarLadder(steps);
