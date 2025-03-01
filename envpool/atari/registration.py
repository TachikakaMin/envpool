# Copyright 2021 Garena Online Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Atari env registration."""

import os

from envpool.registration import register

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

atari_rom_path = os.path.join(base_path, "atari", "atari_roms")
atari_game_list = os.listdir(atari_rom_path)

for game in atari_game_list:
  name = "".join([g.capitalize() for g in game.split("_")])
  register(
    task_id=name + "-v5",
    import_path="envpool.atari",
    spec_cls="AtariEnvSpec",
    dm_cls="AtariDMEnvPool",
    gym_cls="AtariGymEnvPool",
    task=game,
    base_path=base_path,
  )
