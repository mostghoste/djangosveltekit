import { env as publicEnv } from '$env/dynamic/public';

export const API_BASE =
  publicEnv.PUBLIC_API_BASE || 'http://localhost:8000';
