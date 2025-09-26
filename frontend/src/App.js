import React, { useState, useEffect } from 'react';
import OverviewDashboard from './components/Dashboard/OverviewDashboard';
import HostInventory from './components/Dashboard/HostInventory';
import AlertsManager from './components/Dashboard/AlertsManager';
import AnomaliesView from './components/Dashboard/AnomaliesView';
import AnalyticsDashboard from './components/Dashboard/AnalyticsDashboard';

export default function App(){
  const [tab, setTab] = useState('overview');
  return (
    <div className="min-h-screen p-4">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">AI Infra Monitoring</h1>
        <nav>
          {['overview','hosts','alerts','anomalies','analytics'].map(t=>(
            <button key={t} onClick={()=>setTab(t)} className="mx-2">{t}</button>
          ))}
        </nav>
      </header>
      <main className="mt-6">
        {tab==='overview' && <OverviewDashboard/>}
        {tab==='hosts' && <HostInventory/>}
        {tab==='alerts' && <AlertsManager/>}
        {tab==='anomalies' && <AnomaliesView/>}
        {tab==='analytics' && <AnalyticsDashboard/>}
      </main>
    </div>
  );
}
