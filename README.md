# NOTICE
This project is highly inspired from [@benmoran56's esper](https://github.com/benmoran56/esper).  

You can see things in similar between my definition of World and Entity classes and esper's ones so far.  
Thus, I abandon my rights to this project until it is natural to my claiming my rights to this project with its originality.  

# ToDo list

## Phase 0 (learning what it's like to create a game in ECS design method.)
1. [x] Create base component, entity, system class.
2. [x] Create some basic components (PositionComponent, RenderableComponent and VelocityComponent).
3. [x] Create some basic systems (MovementSystem, KeyControlSystem and SoundMixerSystem).
4. [x] Create a mini game that you can control your unit.

## Phase 1 (Making a simple GUI RPG.)
1. [x] Create CollisionSystem that you can handle the collision between any objects.
2. [x] Draw map on screen after parsing tmx and tsx files.(temporarily solved by adopting pytmx)
3. [ ] Add MovementAnimation component and system(add animation to moving objects).
4. [ ] Add StatsComponent where stores stats of an unit like HP, MP, Strength, Wisdom, Intelligence.
5. [ ] Create BattleSystem.
6. [ ] Create SceneComponent and SceneContrlSystem (system includes: start menu handing).