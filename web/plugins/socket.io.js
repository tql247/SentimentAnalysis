import io from 'socket.io-client'
const socket = io(process.env.wsUrl)

export default socket
