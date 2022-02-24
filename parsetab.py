
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD ALTER AND AS COLUMN COMMASTRING COMMENT CREATE DIFFERENT DO DROP END FROM GREATEREQUALTHAN IS LESSEQUALTHAN LOAD MODIFY NUMBER ON OR PROCEDURE SAVE SELECT SHOW TABLE VAR WHERE csvfile A : procedurecommand\n              | multicommand  procedurecommand : PROCEDURE VAR DO multicommand END ';' multicommand : command\n                         | multicommand command command : commandcreate ';'\n                    | commandshow ';'\n                    | commandalter ';'\n                    | commandcomment ';'\n                    | commandsave ';'\n                    | commandselect ';'\n                    | commanddrop ';'\n                    | commandload ';' commandload : LOAD TABLE VAR FROM csvfile commandcreate : CREATE TABLE VAR '(' argument ')'\n                          | CREATE TABLE VAR commandshow : SHOW TABLE VAR  commanddrop : DROP TABLE VAR commandalter : ALTER TABLE VAR ADD COLUMN VAR\n                         | ALTER TABLE VAR DROP COLUMN VAR commandcomment : COMMENT ON TABLE VAR IS comment  commandsave : SAVE TABLE VAR AS csvfile  commandselect : SELECT VAR FROM VAR\n                          | SELECT VAR FROM VAR wherecomparison argument : subargument\n                     |                          \n                     | argument ',' subargument subargument : VAR VAR '(' NUMBER ')'  comment :  COMMASTRING  wherecomparison : WHERE COMPARISON\n                            | WHERE COMPARISON ORAND COMPARISON\n                            |  COMPARISON : VAR '>' NUMBER\n                       | VAR '<' NUMBER\n                       | VAR DIFFERENT NUMBER\n                       | VAR GREATEREQUALTHAN NUMBER\n                       | VAR LESSEQUALTHAN NUMBER ORAND : OR\n                  | AND"
    
_lr_action_items = {'PROCEDURE':([0,],[4,]),'CREATE':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,14,14,]),'SHOW':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,15,15,]),'ALTER':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,16,16,]),'COMMENT':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,18,18,]),'SAVE':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,19,19,]),'SELECT':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,20,20,]),'DROP':([0,3,5,22,24,25,26,27,28,29,30,31,40,43,49,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,17,52,17,]),'LOAD':([0,3,5,22,24,25,26,27,28,29,30,31,40,49,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,21,21,]),'$end':([1,2,3,5,22,24,25,26,27,28,29,30,31,68,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-3,]),'VAR':([4,20,32,33,34,35,37,39,45,47,50,58,61,62,66,71,80,81,82,],[23,38,41,42,43,44,46,48,53,55,58,69,72,73,77,58,77,-38,-39,]),'END':([5,22,24,25,26,27,28,29,30,31,49,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,57,]),';':([6,7,8,9,10,11,12,13,41,42,44,55,57,64,65,67,70,72,73,74,75,76,89,90,91,92,93,94,],[24,25,26,27,28,29,30,31,-16,-17,-18,-23,68,-22,-24,-14,-15,-19,-20,-21,-29,-30,-31,-33,-34,-35,-36,-37,]),'TABLE':([14,15,16,17,19,21,36,],[32,33,34,35,37,39,45,]),'ON':([18,],[36,]),'DO':([23,],[40,]),'FROM':([38,48,],[47,56,]),'(':([41,69,],[50,78,]),'ADD':([43,],[51,]),'AS':([46,],[54,]),')':([50,59,60,79,88,95,],[-26,70,-25,-27,95,-28,]),',':([50,59,60,79,95,],[-26,71,-25,-27,-28,]),'COLUMN':([51,52,],[61,62,]),'IS':([53,],[63,]),'csvfile':([54,56,],[64,67,]),'WHERE':([55,],[66,]),'COMMASTRING':([63,],[75,]),'OR':([76,90,91,92,93,94,],[81,-33,-34,-35,-36,-37,]),'AND':([76,90,91,92,93,94,],[82,-33,-34,-35,-36,-37,]),'>':([77,],[83,]),'<':([77,],[84,]),'DIFFERENT':([77,],[85,]),'GREATEREQUALTHAN':([77,],[86,]),'LESSEQUALTHAN':([77,],[87,]),'NUMBER':([78,83,84,85,86,87,],[88,90,91,92,93,94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'A':([0,],[1,]),'procedurecommand':([0,],[2,]),'multicommand':([0,40,],[3,49,]),'command':([0,3,40,49,],[5,22,5,22,]),'commandcreate':([0,3,40,49,],[6,6,6,6,]),'commandshow':([0,3,40,49,],[7,7,7,7,]),'commandalter':([0,3,40,49,],[8,8,8,8,]),'commandcomment':([0,3,40,49,],[9,9,9,9,]),'commandsave':([0,3,40,49,],[10,10,10,10,]),'commandselect':([0,3,40,49,],[11,11,11,11,]),'commanddrop':([0,3,40,49,],[12,12,12,12,]),'commandload':([0,3,40,49,],[13,13,13,13,]),'argument':([50,],[59,]),'subargument':([50,71,],[60,79,]),'wherecomparison':([55,],[65,]),'comment':([63,],[74,]),'COMPARISON':([66,80,],[76,89,]),'ORAND':([76,],[80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> A","S'",1,None,None,None),
  ('A -> procedurecommand','A',1,'p_A','logic_grammar.py',32),
  ('A -> multicommand','A',1,'p_A','logic_grammar.py',33),
  ('procedurecommand -> PROCEDURE VAR DO multicommand END ;','procedurecommand',6,'p_procedure','logic_grammar.py',42),
  ('multicommand -> command','multicommand',1,'p_multicommand','logic_grammar.py',49),
  ('multicommand -> multicommand command','multicommand',2,'p_multicommand','logic_grammar.py',50),
  ('command -> commandcreate ;','command',2,'p_command','logic_grammar.py',62),
  ('command -> commandshow ;','command',2,'p_command','logic_grammar.py',63),
  ('command -> commandalter ;','command',2,'p_command','logic_grammar.py',64),
  ('command -> commandcomment ;','command',2,'p_command','logic_grammar.py',65),
  ('command -> commandsave ;','command',2,'p_command','logic_grammar.py',66),
  ('command -> commandselect ;','command',2,'p_command','logic_grammar.py',67),
  ('command -> commanddrop ;','command',2,'p_command','logic_grammar.py',68),
  ('command -> commandload ;','command',2,'p_command','logic_grammar.py',69),
  ('commandload -> LOAD TABLE VAR FROM csvfile','commandload',5,'p_load','logic_grammar.py',75),
  ('commandcreate -> CREATE TABLE VAR ( argument )','commandcreate',6,'p_commandcreate','logic_grammar.py',80),
  ('commandcreate -> CREATE TABLE VAR','commandcreate',3,'p_commandcreate','logic_grammar.py',81),
  ('commandshow -> SHOW TABLE VAR','commandshow',3,'p_commandshow','logic_grammar.py',91),
  ('commanddrop -> DROP TABLE VAR','commanddrop',3,'p_commanddrop','logic_grammar.py',96),
  ('commandalter -> ALTER TABLE VAR ADD COLUMN VAR','commandalter',6,'p_commandalter','logic_grammar.py',101),
  ('commandalter -> ALTER TABLE VAR DROP COLUMN VAR','commandalter',6,'p_commandalter','logic_grammar.py',102),
  ('commandcomment -> COMMENT ON TABLE VAR IS comment','commandcomment',6,'p_commandcomment','logic_grammar.py',109),
  ('commandsave -> SAVE TABLE VAR AS csvfile','commandsave',5,'p_commandsave','logic_grammar.py',116),
  ('commandselect -> SELECT VAR FROM VAR','commandselect',4,'p_commandselect','logic_grammar.py',123),
  ('commandselect -> SELECT VAR FROM VAR wherecomparison','commandselect',5,'p_commandselect','logic_grammar.py',124),
  ('argument -> subargument','argument',1,'p_argument','logic_grammar.py',134),
  ('argument -> <empty>','argument',0,'p_argument','logic_grammar.py',135),
  ('argument -> argument , subargument','argument',3,'p_argument','logic_grammar.py',136),
  ('subargument -> VAR VAR ( NUMBER )','subargument',5,'p_subargument','logic_grammar.py',151),
  ('comment -> COMMASTRING','comment',1,'p_comment','logic_grammar.py',160),
  ('wherecomparison -> WHERE COMPARISON','wherecomparison',2,'p_wherecomparison','logic_grammar.py',167),
  ('wherecomparison -> WHERE COMPARISON ORAND COMPARISON','wherecomparison',4,'p_wherecomparison','logic_grammar.py',168),
  ('wherecomparison -> <empty>','wherecomparison',0,'p_wherecomparison','logic_grammar.py',169),
  ('COMPARISON -> VAR > NUMBER','COMPARISON',3,'p_COMPARISON','logic_grammar.py',178),
  ('COMPARISON -> VAR < NUMBER','COMPARISON',3,'p_COMPARISON','logic_grammar.py',179),
  ('COMPARISON -> VAR DIFFERENT NUMBER','COMPARISON',3,'p_COMPARISON','logic_grammar.py',180),
  ('COMPARISON -> VAR GREATEREQUALTHAN NUMBER','COMPARISON',3,'p_COMPARISON','logic_grammar.py',181),
  ('COMPARISON -> VAR LESSEQUALTHAN NUMBER','COMPARISON',3,'p_COMPARISON','logic_grammar.py',182),
  ('ORAND -> OR','ORAND',1,'p_ORAND','logic_grammar.py',186),
  ('ORAND -> AND','ORAND',1,'p_ORAND','logic_grammar.py',187),
]