var addTwoPromises = async function (promise1, promise2) {
    return await Promise.all([promise1, promise2]).then(data => data[0] + data[1])
};

/*
addTwoPromises(Promise.resolve(2), Promise.resolve(2)).then(console.log); // 4
addTwoPromises(Promise.resolve(2), Promise.resolve(5)).then(console.log); // 7
addTwoPromises(Promise.resolve(10), Promise.resolve(-12)).then(console.log); // -2
*/
