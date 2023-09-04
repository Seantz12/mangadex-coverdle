import { useState } from 'react';

function Cover() {
    const [coverURL, setCoverURL] = useState('https://pbs.twimg.com/media/EvEsRgMWQAIWDEu?format=jpg&name=large');

    function getCover() {
        setCoverURL('https://cdn.myanimelist.net/s/common/store/cover/11274/7c0e668dc5af381f1ec4d723e3a298e197066c2059ca39977c7cf5f00081340b/l.jpg')
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