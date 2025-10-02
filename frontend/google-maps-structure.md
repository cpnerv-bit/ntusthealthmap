# 前端 Google Maps API 架構規劃

## 主要功能
1. 顯示台科大校園地圖（Google Maps API）
2. 標記校園建築物（根據資料庫 buildings 表）
3. 顯示建築物解鎖狀態（已解鎖/未解鎖）
4. 顯示使用者探索進度（地圖上進度條或已解鎖建築物高亮）
5. 點擊建築物顯示詳細資訊與解鎖條件
6. 顯示健康挑戰任務與團體任務進度

## 技術建議
- React + Google Maps JavaScript API
- 使用 axios 連接 Flask API
- 狀態管理可用 Redux 或 Context API

## 主要元件
- MapContainer：地圖主元件，載入 Google Maps
- BuildingMarker：建築物標記元件，根據解鎖狀態顯示不同顏色
- ProgressPanel：顯示探索進度、點數、任務
- ChallengePanel：顯示健康挑戰任務
- TeamPanel：顯示團體任務與成員

## API 互動
- 取得建築物列表與座標 `/api/buildings`
- 取得使用者進度 `/api/progress/<user_id>`
- 取得挑戰任務 `/api/challenges`
- 取得團體任務 `/api/team_tasks/<team_id>`

## Google Maps API 使用
- 申請 API 金鑰
- 設定地圖中心點為台科大校園座標
- 根據 buildings 表座標標記建築物
- 根據解鎖狀態高亮顯示

---
此規劃可作為前端開發的架構參考，後續可依需求細化元件設計。
