// web/src/components/Trade.js
import React, { useState } from 'react';
import web3 from '../utils/web3';

const Trade = () => {
    const [sender, setSender] = useState('');
    const [receiver, setReceiver] = useState('');
    const [amount, setAmount] = useState('');

    const handleTrade = async () => {
        const accounts = await web3.eth.getAccounts();
        // Add logic to trade tokens on the blockchain
        console.log('Trade executed');
    };

    return (
        <div>
            <h1>Trade Tokens</h1>
            <input placeholder="Sender" value={sender} onChange={(e) => setSender(e.target.value)} />
            <input placeholder="Receiver" value={receiver} onChange={(e) => setReceiver(e.target.value)} />
            <input placeholder="Amount" value={amount} onChange={(e) => setAmount(e.target.value)} />
            <button onClick={handleTrade}>Trade</button>
        </div>
    );
};

export default Trade;

