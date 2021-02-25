import { NextApiRequest, NextApiResponse } from 'next'
import { stringify } from 'query-string';
import getConfig from "next/config";


export default async (req: NextApiRequest, res: NextApiResponse) => {
    const { publicRuntimeConfig } = getConfig();
    const { method } = req
    const query = req.query
    let data;
    switch (method) {
      case 'GET':
        data = await fetch('http://' + publicRuntimeConfig.API_URL  + `/api/v1/cars?${stringify(query)}`);
        return res.status(data.status).json(await data.json());
      case 'POST':
        data = await fetch('http://' + publicRuntimeConfig.API_URL  + `/api/v1/cars`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(req.body),
        })  
        return res.status(data.status).json(await data.json());        
      default:
        res.setHeader('Allow', ['GET', 'POST'])
        res.status(405).end(`Method ${method} Not Allowed`)    
    }
}
