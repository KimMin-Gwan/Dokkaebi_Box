const path = require('path')

module.exports = {
    resolve: {
        fallback: {
            util: require.resolve("util/"),
            crypto: require.resolve("crypto-browserify"),
            url: require.resolve("url/"),
            http: require.resolve("stream-http"),
            https: require.resolve("https-browserify"),
            path: require.resolve("path-browserify"),
            fs: false, // 또는 require.resolve("path-browserify")
        },
    },
}
