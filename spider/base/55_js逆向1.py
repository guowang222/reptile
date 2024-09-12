
js = '''
  function l(t, e) {
                var n = (65535 & t) + (65535 & e);
                return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
            }
            function a(t, e, n, o, r, i) {
                return l((s = l(l(e, t), l(o, i))) << (a = r) | s >>> 32 - a, n);
                var s, a
            }
            function f(t, e, n, o, r, i, s) {
                return a(e & n | ~e & o, t, e, r, i, s)
            }
            function d(t, e, n, o, r, i, s) {
                return a(e & o | n & ~o, t, e, r, i, s)
            }
            function h(t, e, n, o, r, i, s) {
                return a(e ^ n ^ o, t, e, r, i, s)
            }
            function m(t, e, n, o, r, i, s) {
                return a(n ^ (e | ~o), t, e, r, i, s)
            }
            function c(t, e) {
                t[e >> 5] |= 128 << e % 32,
                t[14 + (e + 64 >>> 9 << 4)] = e;
                var n, o, r, i, s, a = 1732584193, c = -271733879, u = -1732584194, p = 271733878;
                for (n = 0; n < t.length; n += 16)
                    a = f(o = a, r = c, i = u, s = p, t[n], 7, -680876936),
                    p = f(p, a, c, u, t[n + 1], 12, -389564586),
                    u = f(u, p, a, c, t[n + 2], 17, 606105819),
                    c = f(c, u, p, a, t[n + 3], 22, -1044525330),
                    a = f(a, c, u, p, t[n + 4], 7, -176418897),
                    p = f(p, a, c, u, t[n + 5], 12, 1200080426),
                    u = f(u, p, a, c, t[n + 6], 17, -1473231341),
                    c = f(c, u, p, a, t[n + 7], 22, -45705983),
                    a = f(a, c, u, p, t[n + 8], 7, 1770035416),
                    p = f(p, a, c, u, t[n + 9], 12, -1958414417),
                    u = f(u, p, a, c, t[n + 10], 17, -42063),
                    c = f(c, u, p, a, t[n + 11], 22, -1990404162),
                    a = f(a, c, u, p, t[n + 12], 7, 1804603682),
                    p = f(p, a, c, u, t[n + 13], 12, -40341101),
                    u = f(u, p, a, c, t[n + 14], 17, -1502002290),
                    a = d(a, c = f(c, u, p, a, t[n + 15], 22, 1236535329), u, p, t[n + 1], 5, -165796510),
                    p = d(p, a, c, u, t[n + 6], 9, -1069501632),
                    u = d(u, p, a, c, t[n + 11], 14, 643717713),
                    c = d(c, u, p, a, t[n], 20, -373897302),
                    a = d(a, c, u, p, t[n + 5], 5, -701558691),
                    p = d(p, a, c, u, t[n + 10], 9, 38016083),
                    u = d(u, p, a, c, t[n + 15], 14, -660478335),
                    c = d(c, u, p, a, t[n + 4], 20, -405537848),
                    a = d(a, c, u, p, t[n + 9], 5, 568446438),
                    p = d(p, a, c, u, t[n + 14], 9, -1019803690),
                    u = d(u, p, a, c, t[n + 3], 14, -187363961),
                    c = d(c, u, p, a, t[n + 8], 20, 1163531501),
                    a = d(a, c, u, p, t[n + 13], 5, -1444681467),
                    p = d(p, a, c, u, t[n + 2], 9, -51403784),
                    u = d(u, p, a, c, t[n + 7], 14, 1735328473),
                    a = h(a, c = d(c, u, p, a, t[n + 12], 20, -1926607734), u, p, t[n + 5], 4, -378558),
                    p = h(p, a, c, u, t[n + 8], 11, -2022574463),
                    u = h(u, p, a, c, t[n + 11], 16, 1839030562),
                    c = h(c, u, p, a, t[n + 14], 23, -35309556),
                    a = h(a, c, u, p, t[n + 1], 4, -1530992060),
                    p = h(p, a, c, u, t[n + 4], 11, 1272893353),
                    u = h(u, p, a, c, t[n + 7], 16, -155497632),
                    c = h(c, u, p, a, t[n + 10], 23, -1094730640),
                    a = h(a, c, u, p, t[n + 13], 4, 681279174),
                    p = h(p, a, c, u, t[n], 11, -358537222),
                    u = h(u, p, a, c, t[n + 3], 16, -722521979),
                    c = h(c, u, p, a, t[n + 6], 23, 76029189),
                    a = h(a, c, u, p, t[n + 9], 4, -640364487),
                    p = h(p, a, c, u, t[n + 12], 11, -421815835),
                    u = h(u, p, a, c, t[n + 15], 16, 530742520),
                    a = m(a, c = h(c, u, p, a, t[n + 2], 23, -995338651), u, p, t[n], 6, -198630844),
                    p = m(p, a, c, u, t[n + 7], 10, 1126891415),
                    u = m(u, p, a, c, t[n + 14], 15, -1416354905),
                    c = m(c, u, p, a, t[n + 5], 21, -57434055),
                    a = m(a, c, u, p, t[n + 12], 6, 1700485571),
                    p = m(p, a, c, u, t[n + 3], 10, -1894986606),
                    u = m(u, p, a, c, t[n + 10], 15, -1051523),
                    c = m(c, u, p, a, t[n + 1], 21, -2054922799),
                    a = m(a, c, u, p, t[n + 8], 6, 1873313359),
                    p = m(p, a, c, u, t[n + 15], 10, -30611744),
                    u = m(u, p, a, c, t[n + 6], 15, -1560198380),
                    c = m(c, u, p, a, t[n + 13], 21, 1309151649),
                    a = m(a, c, u, p, t[n + 4], 6, -145523070),
                    p = m(p, a, c, u, t[n + 11], 10, -1120210379),
                    u = m(u, p, a, c, t[n + 2], 15, 718787259),
                    c = m(c, u, p, a, t[n + 9], 21, -343485551),
                    a = l(a, o),
                    c = l(c, r),
                    u = l(u, i),
                    p = l(p, s);
                return [a, c, u, p]
            }
            function u(t) {
                var e, n = "";
                for (e = 0; e < 32 * t.length; e += 8)
                    n += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
                return n
            }
            function p(t) {
                var e, n = [];
                for (n[(t.length >> 2) - 1] = void 0,
                e = 0; e < n.length; e += 1)
                    n[e] = 0;
                for (e = 0; e < 8 * t.length; e += 8)
                    n[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
                return n
            }
            function o(t) {
                var e, n, o = "0123456789abcdef", r = "";
                for (n = 0; n < t.length; n += 1)
                    e = t.charCodeAt(n),
                    r += o.charAt(e >>> 4 & 15) + o.charAt(15 & e);
                return r
            }
            function r(t) {
                return unescape(encodeURIComponent(t))
            }
            function i(t) {
                return u(c(p(e = r(t)), 8 * e.length));
                var e
            }
            function s(t, e) {
                return function(t, e) {
                    var n, o, r = p(t), i = [], s = [];
                    for (i[15] = s[15] = void 0,
                    16 < r.length && (r = c(r, 8 * t.length)),
                    n = 0; n < 16; n += 1)
                        i[n] = 909522486 ^ r[n],
                        s[n] = 1549556828 ^ r[n];
                    return o = c(i.concat(p(e)), 512 + 8 * e.length),
                    u(c(s.concat(o), 640))
                }(r(t), r(e))
            }
n.exports = get_pwd(t, e, n) {
            return e ? n ? s(e, t) : o(s(e, t)) : n ? i(t) : o(i(t))
}

'''

import execjs

ctx = execjs.compile(js)
rs = ctx.call('n.exports','123456')
print(rs)

# 如果需要使用 node命令，需要提前安装node.js 软件