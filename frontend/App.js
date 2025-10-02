import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MapContainer from './MapContainer';

// 請將 YOUR_API_KEY 替換為你的 Google Maps API 金鑰
// MapContainer 會自動載入地圖與標記

function App() {
  const [buildings, setBuildings] = useState([]);
  const [progress, setProgress] = useState([]);
  const userId = 1; // 範例用，實際應由登入取得

  useEffect(() => {
    axios.get('http://localhost:5000/progress/' + userId)
      .then(res => setProgress(res.data.progress));
    axios.get('http://localhost:5000/buildings')
      .then(res => setBuildings(res.data.buildings));
  }, []);

  // 取得已解鎖建築物 id 陣列
  const unlockedIds = progress
    .filter(p => p.unlocked_building_id)
    .map(p => p.unlocked_building_id);

  return (
    <div>
      <h1>健康任務地圖</h1>
      {/* Google Maps 地圖元件，請先在 MapContainer.js 填入你的 API 金鑰 */}
      <MapContainer buildings={buildings} unlockedIds={unlockedIds} />
      <div>
        <h2>探索進度</h2>
        {progress.map(p => (
          <div key={p.id}>
            日期：{p.date}，步數：{p.steps}，運動：{p.exercise_minutes} 分鐘，喝水：{p.water_ml} ml
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;