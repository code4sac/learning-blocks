import logLevel from 'loglevel'

export const log = logLevel.getLogger('trashai')
log.setLevel('debug')
// if (import.meta.env.DEV) {
//     log.setLevel('debug')
// } else {
//     log.setLevel('info')
// }