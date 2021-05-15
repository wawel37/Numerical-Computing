const puppeteer = require('puppeteer');
const fs = require('fs');

async function getDataSet(documentNumber, dataFilePath, linkFilePath, buffCleanInterval){
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const URL = 'https://simple.wikipedia.org/wiki/Special:Random';
    //const URL = 'https://pl.wikipedia.org/wiki/Alpy_Berchtesgade%C5%84skie';

    let dataBuff = '';
    let linkBuff = '';
    let duplicateMap = new Map();

    for(let i = 0; i < documentNumber; i++){

        await page.goto(URL, { waitUntil: 'networkidle2'});

        let docData = await page.evaluate(async () => {
            let title = document.getElementById('firstHeading').innerText;
            let content = document.getElementById('mw-content-text').childNodes[0].getElementsByTagName('p');

            content = Object.keys(content)
            .map(key => content[key].innerText)
            .join('\n');
            
            //title = title.replace('[edytuj]', '');

            //No need to remove second title, because not always the "-" is present
            // content = content.split('–');
            // content.splice(0,1);
            // content = content
            // .join('-')
            content = content.replace(new RegExp("\[[0-9]*\]", "g"), '');

            return {
                title,
                content
            };

        });
        docData['url'] = await page.url();

        
        if(duplicateMap.has(docData.title)){
            console.log("Duplicate title: " + docData.title);
            continue;
        }else{
            duplicateMap.set(docData.title, true);
        }

        dataBuff += docData.title + "\n";

        for(doc of docData.content){
            dataBuff += doc;
        }
        dataBuff += "\n";

        linkBuff += docData.url + "\n";

        console.log("Document nr " + (i + 1) + " processed");


        if((i + 1) % buffCleanInterval == 0){
            fs.appendFileSync(dataFilePath, dataBuff);
            fs.appendFileSync(linkFilePath, linkBuff);

            dataBuff = '';
            linkBuff = '';
            
            console.log('Appending to file ' + buffCleanInterval + ' documents');
        }
    }
    
    await browser.close();
}

getDataSet(50000, 'data-eng.txt', 'links-eng.txt', 10);
  