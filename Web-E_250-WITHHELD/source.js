function password(e) {
    if (e.length != 19) {
        return false
    }
    if (e.charAt(6) != e.charAt(12)) {
        return false
    }
    if (e.charCodeAt(10) != 95) {
        return false
    }
    if (e.charCodeAt(3) - e.charCodeAt(5) != (e.charCodeAt(17) - e.charCodeAt(11)) * 9) {
        return false
    }
    if (e.charCodeAt(5) + e.charCodeAt(11) + e.charCodeAt(17) != 293) {
        return false
    }
    if (e.charCodeAt(17) - e.charCodeAt(11) + e.charCodeAt(5) != 69) {
        return false
    }
    if (e.charCodeAt(3) != e.charCodeAt(18) - 15) {
        return false
    }
    var data = [];
    var data2 = [];
    for (i = 0; i < e.length; i = i + 2) {
        data.push(e.charCodeAt(i))
    }
    for (i = 1; i < e.length; i = i + 2) {
        data2.push(e.charCodeAt(i))
    }
    if (data[0] != data[8]) {
        return false
    }
    if (data2[4] != data[9]) {
        return false
    }
    if ((data[0] & data[3]) != (data[0] - Math.pow(2, 4))) {
        return false
    }
    if ((data[1] | data[2]) != data2[7]) {
        return false
    }
    if ((data[3] >> 1) != (data[0] << 1) / 2) {
        return false
    }
    if ((data[2] & data[3]) != data[6]) {
        return false
    }
    if ((e.charCodeAt(10) ^ data[2]) != 42 + 2) {
        return false
    }
    if (data[2] != data2[6]) {
        return false
    }
    if ((data[8] | 1) != (data[8] + 1)) {
        return false
    }
    if (String.fromCharCode(data2[6]).toUpperCase() != e.charAt(14)) {
        return false
    }
    if ((data2[6] >> 5) * 34 != data[1]) {
        return false
    }
    if ((((data2[0] % 7) + 3) | data[8]) != data[4]) {
        return false
    }
    if ((data[1] + data2[0]) / 2 != data[9]) {
        return false
    }
    if (data[9] % 10 !== 0) {
        return false
    }
    if (data[4] != data[1] / 2) {
        return false
    }
    return true
};
