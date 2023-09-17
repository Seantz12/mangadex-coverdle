import { useState } from 'react';
// const MFA = require('mangadex-full-api');

function Cover() {
    const [coverURL, setCoverURL] = useState('https://pbs.twimg.com/media/EvEsRgMWQAIWDEu?format=jpg&name=large');

    async function getCover() {
        // MFA.Cover.get('683a613e-8aa0-4b98-9a62-4138463d6a49');
        const url = 'http://localhost:1617/get-random-cover';
        const response = await fetch(url, {
                method: "GET",
                mode: "cors"
            }
        );
        const data = await response.json();
        setCoverURL(data["message"]);
    }

    return (
        <section>
            <img src={coverURL}/>
            <h1>test</h1>
            <button onClick={getCover}> test test test</button>
        </section>
    );
}

export default Cover;