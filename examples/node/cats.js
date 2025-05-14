function print_at_location(col,text) {
    console.log(' '.repeat(col) + text);
}

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

function clear_term() {
    process.stdout.write('\x1Bc')
}

async function animate() {
    const width = parseInt(process.stdout.columns, 10);
    // draw the pet
}

animate(); // Call the async function