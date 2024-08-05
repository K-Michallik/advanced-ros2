import { ApplicationNode } from '@universal-robots/contribution-api';

export interface Ros2CommunicatorNode extends ApplicationNode {
  type: string;
  version: string;
}
