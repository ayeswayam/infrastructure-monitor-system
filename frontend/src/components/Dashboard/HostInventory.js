import React, {useEffect, useState} from 'react';
import axios from 'axios';
export default function HostInventory(){
  const [hosts, setHosts] = useState([]);
  useEffect(()=>{ axios.get('/api/v1/hosts').then(r=>setHosts(r.data)).catch(()=>{});},[]);
  return <div><h2>Hosts</h2><table><thead><tr><th>Hostname</th><th>IP</th></tr></thead><tbody>{hosts.map(h=>(<tr key={h.id}><td>{h.hostname}</td><td>{h.ip_address}</td></tr>))}</tbody></table></div>;
}
