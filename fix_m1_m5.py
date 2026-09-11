#!/usr/bin/env python3
"""Replace Module 1 and Module 5 with deeply detailed, Module-3-level content."""

with open('VIPmembers.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 1 — polished & deeply detailed replacement
# ─────────────────────────────────────────────────────────────────────────────
NEW_MODULE_1 = """            <div class="module-content-pane active" id="module-1">
                <div class="module-hero">
                    <span class="module-number">The Foundation</span>
                    <h1>Module 1: Foundation of an Institutional Trader</h1>
                    <p>Dismantle every retail myth. Understand the true $7.5T architecture, the IPDA algorithmic price delivery cycle, and the operator mindset that separates the top 1% from the 90% who chronically lose.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 12.5%;"></div>
                    </div>
                </div>

                <!-- 1. TRUE ARCHITECTURE -->
                <div class="content-section">
                    <h3><i class='bx bx-globe'></i> 1. The True Architecture of the $7.5 Trillion FX Market</h3>
                    <p>Forex is the largest, most liquid financial market on Earth — yet it is completely <strong>opaque</strong> and <strong>decentralised</strong>. There is no central exchange. Every transaction is settled through a layered interbank network, and the players at each layer operate with fundamentally different information, tools, and intentions.</p>

                    <div class="key-takeaways">
                        <h4>🔑 The Critical Reality Every Retail Trader Misses</h4>
                        <p style="font-size:13px;color:#ccc;">Retail traders represent less than <strong style="color:var(--vip-gold)">5%</strong> of daily FX volume. The remaining 95% is institutional. Every time a retail trader clicks "Buy," a Tier-1 prime brokerage or algorithm is on the other side of that trade — <em>with a structural information advantage</em>.</p>
                    </div>

                    <!-- Pyramid SVG -->
                    <div class="illustration-container">
                        <div style="background:#080808;border:1px solid #222;border-radius:16px;padding:24px;overflow-x:auto;">
                            <svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;min-width:500px;height:auto;display:block;">
                                <defs>
                                    <linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="0%" stop-color="#D6FF00" stop-opacity="0.25"/>
                                        <stop offset="100%" stop-color="#D6FF00" stop-opacity="0.04"/>
                                    </linearGradient>
                                </defs>
                                <!-- Tier 1 -->
                                <polygon points="350,28 430,100 270,100" fill="url(#goldGrad)" stroke="#D6FF00" stroke-width="2"/>
                                <text x="350" y="65" fill="#D6FF00" font-size="13" font-weight="700" text-anchor="middle">TIER 1 BANKS</text>
                                <text x="350" y="82" fill="#999" font-size="10" text-anchor="middle">JPMorgan · Deutsche · Citi · UBS</text>
                                <text x="450" y="70" fill="#888" font-size="10">~40% of Volume</text>

                                <!-- Tier 2 -->
                                <polygon points="270,100 430,100 490,165 210,165" fill="rgba(255,255,255,0.04)" stroke="#444" stroke-width="1.2"/>
                                <text x="350" y="133" fill="#eee" font-size="12" font-weight="600" text-anchor="middle">CENTRAL BANKS &amp; SOVEREIGN FUNDS</text>
                                <text x="350" y="152" fill="#999" font-size="10" text-anchor="middle">Macro Policy · Forex Reserves · Sterilisation</text>
                                <text x="510" y="140" fill="#888" font-size="10">~20% of Volume</text>

                                <!-- Tier 3 -->
                                <polygon points="210,165 490,165 555,235 145,235" fill="rgba(255,255,255,0.025)" stroke="#333" stroke-width="1"/>
                                <text x="350" y="202" fill="#ccc" font-size="12" font-weight="600" text-anchor="middle">HEDGE FUNDS &amp; ASSET MANAGERS</text>
                                <text x="350" y="220" fill="#999" font-size="10" text-anchor="middle">Directional Specs · Macro Funds · CTA Algos</text>
                                <text x="570" y="208" fill="#888" font-size="10">~25% of Volume</text>

                                <!-- Retail Zone -->
                                <rect x="80" y="245" width="540" height="40" rx="6" fill="rgba(255,50,50,0.08)" stroke="#ff3333" stroke-width="1.5" stroke-dasharray="5,3"/>
                                <text x="350" y="262" fill="#ff3333" font-size="12" font-weight="700" text-anchor="middle">RETAIL TRADERS — THE LIQUIDITY POOL</text>
                                <text x="350" y="278" fill="#cc3333" font-size="10" text-anchor="middle">Stop-loss fuel · Trapped orders · &lt; 5% of volume</text>

                                <!-- Arrows showing flow -->
                                <path d="M 640 265 L 640 108" stroke="#D6FF00" stroke-width="1.5" stroke-dasharray="4,3" fill="none" marker-end="url(#arrowGold)"/>
                                <text x="650" y="190" fill="#D6FF00" font-size="10" font-weight="700" transform="rotate(90,650,190)">VALUE FLOWS UP</text>
                                <defs>
                                    <marker id="arrowGold" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                                        <polygon points="0,0 8,4 0,8" fill="#D6FF00"/>
                                    </marker>
                                </defs>
                            </svg>
                        </div>
                        <p style="font-size:11px;color:#555;margin-top:10px;text-align:center;">The Institutional Hierarchy: Every tier exploits the one below it. Retail traders are the permanent liquidity source at the base.</p>
                    </div>

                    <!-- Tier Breakdown Table -->
                    <div class="sd-table-container" style="margin-top:20px;">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Player</th>
                                    <th>Primary Tool</th>
                                    <th>Information Edge</th>
                                    <th>Retail Relationship</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Tier-1 Prime Banks</strong></td>
                                    <td>Central Limit Order Book (CLOB)</td>
                                    <td>Full order flow visibility, dark pool access</td>
                                    <td><span class="badge-c">Hunts retail stops</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Central Banks</strong></td>
                                    <td>Rate decisions, open market ops</td>
                                    <td>Monetary policy before announcement</td>
                                    <td><span class="badge-c">Triggers macro displacement</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Hedge Funds / CTAs</strong></td>
                                    <td>Proprietary algorithms, quant models</td>
                                    <td>Non-public positioning data</td>
                                    <td><span class="badge-b">Trend that retail chases</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Retail Traders</strong></td>
                                    <td>Lagging indicators, chart patterns</td>
                                    <td>Delayed, public information only</td>
                                    <td><span class="badge-aaa" style="color:#ff3333;border-color:#ff3333;background:rgba(255,50,50,0.1);">Permanent liquidity source</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 2. HOW PRICE ACTUALLY MOVES -->
                <div class="content-section">
                    <h3><i class='bx bx-analyse'></i> 2. How Price ACTUALLY Moves — IPDA &amp; The Delivery Engine</h3>
                    <p>Price is not moved by retail supply and demand. It is delivered by the <strong>Interbank Price Delivery Algorithm (IPDA)</strong> — a suite of high-frequency matching engines running across multiple ECNs simultaneously. The algorithm has one primary objective: <em>seek the highest concentration of resting orders and consume them efficiently</em>.</p>

                    <!-- IPDA Cycle SVG -->
                    <div class="illustration-container">
                        <div style="background:#080808;border:1px solid #222;border-radius:16px;padding:24px;overflow-x:auto;">
                            <svg viewBox="0 0 750 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;min-width:600px;height:auto;display:block;">
                                <defs>
                                    <marker id="aG" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#D6FF00"/></marker>
                                    <marker id="aR" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#ff4444"/></marker>
                                    <marker id="aW" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#aaa"/></marker>
                                </defs>
                                <!-- Phase boxes -->
                                <!-- 1. Consolidation -->
                                <rect x="20" y="80" width="130" height="60" rx="8" fill="rgba(214,255,0,0.06)" stroke="#D6FF00" stroke-width="1.5"/>
                                <text x="85" y="107" fill="#D6FF00" font-size="12" font-weight="700" text-anchor="middle">CONSOLIDATION</text>
                                <text x="85" y="122" fill="#999" font-size="10" text-anchor="middle">Liquidity builds</text>
                                <text x="85" y="135" fill="#777" font-size="9" text-anchor="middle">both sides of range</text>

                                <!-- Arrow 1 -->
                                <line x1="150" y1="110" x2="188" y2="110" stroke="#D6FF00" stroke-width="1.5" marker-end="url(#aG)"/>

                                <!-- 2. Manipulation -->
                                <rect x="190" y="80" width="130" height="60" rx="8" fill="rgba(255,68,68,0.06)" stroke="#ff4444" stroke-width="1.5"/>
                                <text x="255" y="107" fill="#ff4444" font-size="12" font-weight="700" text-anchor="middle">MANIPULATION</text>
                                <text x="255" y="122" fill="#999" font-size="10" text-anchor="middle">False breakout sweep</text>
                                <text x="255" y="135" fill="#777" font-size="9" text-anchor="middle">traps retail traders</text>

                                <!-- Arrow 2 -->
                                <line x1="320" y1="110" x2="358" y2="110" stroke="#aaa" stroke-width="1.5" marker-end="url(#aW)"/>

                                <!-- 3. Displacement -->
                                <rect x="360" y="80" width="130" height="60" rx="8" fill="rgba(255,255,255,0.04)" stroke="#888" stroke-width="1.5"/>
                                <text x="425" y="107" fill="#eee" font-size="12" font-weight="700" text-anchor="middle">DISPLACEMENT</text>
                                <text x="425" y="122" fill="#999" font-size="10" text-anchor="middle">Institutional execution</text>
                                <text x="425" y="135" fill="#777" font-size="9" text-anchor="middle">ERC candle + CHoCH</text>

                                <!-- Arrow 3 -->
                                <line x1="490" y1="110" x2="528" y2="110" stroke="#00ff88" stroke-width="1.5" marker-end="url(#aW)"/>

                                <!-- 4. Distribution -->
                                <rect x="530" y="80" width="130" height="60" rx="8" fill="rgba(0,255,136,0.06)" stroke="#00ff88" stroke-width="1.5"/>
                                <text x="595" y="107" fill="#00ff88" font-size="12" font-weight="700" text-anchor="middle">DISTRIBUTION</text>
                                <text x="595" y="122" fill="#999" font-size="10" text-anchor="middle">True directional move</text>
                                <text x="595" y="135" fill="#777" font-size="9" text-anchor="middle">targets opposing PD array</text>

                                <!-- Phase labels -->
                                <text x="85" y="68" fill="#777" font-size="10" text-anchor="middle" font-style="italic">Phase 1</text>
                                <text x="255" y="68" fill="#777" font-size="10" text-anchor="middle" font-style="italic">Phase 2</text>
                                <text x="425" y="68" fill="#777" font-size="10" text-anchor="middle" font-style="italic">Phase 3</text>
                                <text x="595" y="68" fill="#777" font-size="10" text-anchor="middle" font-style="italic">Phase 4</text>

                                <!-- Bottom annotation -->
                                <text x="375" y="190" fill="#555" font-size="11" text-anchor="middle">IPDA Delivery Cycle — Repeats on every timeframe simultaneously</text>
                            </svg>
                        </div>
                        <p style="font-size:11px;color:#555;margin-top:10px;text-align:center;">The 4-Phase IPDA Cycle: Phase 2 (Manipulation) is where retail losses are created. Phase 3–4 is where institutional profit is extracted.</p>
                    </div>

                    <div class="grid-2" style="margin-top:20px;">
                        <div class="example-box" style="border-left:4px solid #ff3333;">
                            <h4 style="color:#ff3333;">❌ The Retail Narrative</h4>
                            <p style="font-size:13px;color:#888;line-height:1.7;">"Price broke the previous high — this is a strong bullish signal. I'll buy here with my stop below the breakout candle."</p>
                            <div style="margin-top:10px;padding:10px;background:rgba(255,50,50,0.08);border-radius:8px;font-size:12px;color:#ff4444;">
                                <strong>Result:</strong> Price immediately reverses after the breakout, triggering your stop. You exit with a loss. Institutions just used your buy order to exit their long position at a better price.
                            </div>
                        </div>
                        <div class="example-box" style="border-left:4px solid #D6FF00;">
                            <h4 style="color:var(--vip-gold);">✅ The Institutional Reality</h4>
                            <p style="font-size:13px;color:#ccc;line-height:1.7;">"The breakout is a programmed liquidity sweep to fill resting sell-stop orders above the high. Once filled, the IPDA will reverse to deliver price back toward the imbalance zone below."</p>
                            <div style="margin-top:10px;padding:10px;background:rgba(214,255,0,0.05);border-radius:8px;font-size:12px;color:var(--vip-gold);">
                                <strong>Result:</strong> You wait for the displacement candle (CHoCH) and enter short at the new LTF supply zone — capturing 1:5 RR while retail bleeds.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 3. AMD CYCLE -->
                <div class="content-section">
                    <h3><i class='bx bx-cycling'></i> 3. The AMD Model: Accumulation, Manipulation &amp; Distribution</h3>
                    <p>Every significant price move in any liquid market is preceded by a 3-phase institutional cycle. Mastering the visual identification of each phase is the single most powerful skill a trader can develop.</p>

                    <!-- AMD SVG -->
                    <div class="illustration-container">
                        <div style="background:#080808;border:1px solid #222;border-radius:16px;padding:24px;overflow-x:auto;">
                            <svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg" style="width:100%;min-width:560px;height:auto;display:block;">
                                <defs>
                                    <marker id="arrowG2" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#00ff88"/></marker>
                                    <marker id="arrowR2" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#ff4444"/></marker>
                                </defs>
                                <!-- Background zones -->
                                <rect x="20" y="90" width="200" height="100" rx="6" fill="rgba(214,255,0,0.04)" stroke="#D6FF00" stroke-dasharray="4,3" stroke-width="1.2"/>
                                <text x="120" y="78" fill="#D6FF00" font-size="12" font-weight="700" text-anchor="middle">ACCUMULATION</text>
                                <text x="120" y="93" fill="#777" font-size="10" text-anchor="middle">Tight ranging · stops building on both sides</text>

                                <!-- Candlesticks in Accumulation -->
                                <line x1="60" y1="110" x2="60" y2="170" stroke="#888" stroke-width="1"/>
                                <rect x="53" y="118" width="14" height="20" rx="2" fill="#666"/>
                                <line x1="90" y1="108" x2="90" y2="172" stroke="#888" stroke-width="1"/>
                                <rect x="83" y="116" width="14" height="22" rx="2" fill="#555"/>
                                <line x1="120" y1="112" x2="120" y2="168" stroke="#888" stroke-width="1"/>
                                <rect x="113" y="119" width="14" height="18" rx="2" fill="#D6FF00" opacity="0.6"/>
                                <line x1="150" y1="109" x2="150" y2="174" stroke="#888" stroke-width="1"/>
                                <rect x="143" y="117" width="14" height="21" rx="2" fill="#555"/>
                                <line x1="180" y1="111" x2="180" y2="169" stroke="#888" stroke-width="1"/>
                                <rect x="173" y="118" width="14" height="19" rx="2" fill="#D6FF00" opacity="0.6"/>

                                <!-- Manipulation zone -->
                                <rect x="220" y="30" width="160" height="205" rx="6" fill="rgba(255,68,68,0.04)" stroke="#ff4444" stroke-dasharray="4,3" stroke-width="1.2"/>
                                <text x="300" y="20" fill="#ff4444" font-size="12" font-weight="700" text-anchor="middle">MANIPULATION</text>
                                <text x="300" y="35" fill="#777" font-size="10" text-anchor="middle">False sweep · stop cascade</text>

                                <!-- Manipulation candles — spike down then reverse -->
                                <line x1="250" y1="100" x2="250" y2="155" stroke="#888" stroke-width="1"/>
                                <rect x="243" y="108" width="14" height="22" rx="2" fill="#ff4444"/>
                                <line x1="280" y1="90" x2="280" y2="210" stroke="#ff4444" stroke-width="1.5"/>
                                <rect x="273" y="120" width="14" height="60" rx="2" fill="#ff4444"/>
                                <text x="280" y="222" fill="#ff4444" font-size="9" text-anchor="middle">SWEEP</text>
                                <!-- Displacement candle -->
                                <line x1="320" y1="50" x2="320" y2="185" stroke="#00ff88" stroke-width="2"/>
                                <rect x="312" y="55" width="16" height="80" rx="2" fill="#00ff88"/>
                                <text x="342" y="42" fill="#00ff88" font-size="9" font-weight="700">CHoCH</text>
                                <line x1="350" y1="60" x2="350" y2="120" stroke="#00ff88" stroke-width="1.5"/>
                                <rect x="343" y="65" width="14" height="40" rx="2" fill="#00ff88" opacity="0.7"/>

                                <!-- Distribution zone -->
                                <rect x="380" y="20" width="320" height="90" rx="6" fill="rgba(0,255,136,0.04)" stroke="#00ff88" stroke-dasharray="4,3" stroke-width="1.2"/>
                                <text x="540" y="10" fill="#00ff88" font-size="12" font-weight="700" text-anchor="middle">DISTRIBUTION</text>
                                <text x="540" y="25" fill="#777" font-size="10" text-anchor="middle">True directional delivery · 1:5+ RR captured here</text>
                                <line x1="400" y1="90" x2="400" y2="35" stroke="#00ff88" stroke-width="2"/>
                                <rect x="393" y="38" width="14" height="50" rx="2" fill="#00ff88"/>
                                <line x1="430" y1="80" x2="430" y2="28" stroke="#00ff88" stroke-width="2"/>
                                <rect x="423" y="30" width="14" height="48" rx="2" fill="#00ff88"/>
                                <line x1="460" y1="70" x2="460" y2="22" stroke="#00ff88" stroke-width="1.5"/>
                                <rect x="453" y="24" width="14" height="44" rx="2" fill="#00ff88" opacity="0.8"/>
                                <line x1="490" y1="62" x2="490" y2="20" stroke="#00ff88" stroke-width="1.5"/>
                                <rect x="483" y="22" width="14" height="38" rx="2" fill="#00ff88" opacity="0.7"/>
                                <line x1="520" y1="58" x2="520" y2="18" stroke="#00ff88" stroke-width="1.5"/>
                                <rect x="513" y="20" width="14" height="36" rx="2" fill="#D6FF00" opacity="0.7"/>

                                <!-- Entry arrow -->
                                <path d="M 360 135 L 398 55" stroke="#D6FF00" stroke-width="2" fill="none" marker-end="url(#arrowG2)"/>
                                <text x="335" y="155" fill="#D6FF00" font-size="10" font-weight="700">ENTRY HERE</text>

                                <!-- Bottom label -->
                                <text x="360" y="248" fill="#444" font-size="11" text-anchor="middle">EdgeGrid trades the transition from Phase 2 → Phase 3 exclusively</text>
                            </svg>
                        </div>
                        <p style="font-size:11px;color:#555;margin-top:10px;text-align:center;">The AMD Cycle — present on every timeframe from M1 to Monthly. Master this and you see the market as an institutional operator.</p>
                    </div>

                    <div class="sd-table-container" style="margin-top:20px;">
                        <table class="sd-table">
                            <thead>
                                <tr><th>Phase</th><th>What's Happening</th><th>Who's Acting</th><th>Retail Mistake</th><th>EdgeGrid Action</th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong style="color:var(--vip-gold);">Accumulation</strong></td>
                                    <td>Institutions building large position quietly inside a tight range</td>
                                    <td>Tier-1 banks placing passive limit orders in CLOB</td>
                                    <td>"Market is dead — nothing happening"</td>
                                    <td><span class="badge-b">Identify &amp; mark the range</span></td>
                                </tr>
                                <tr>
                                    <td><strong style="color:#ff4444;">Manipulation</strong></td>
                                    <td>Price sweeps one side of the range to harvest stop-loss liquidity</td>
                                    <td>IPDA algo executes false breakout to trigger resting orders</td>
                                    <td>"Breakout — going long!" (gets stopped instantly)</td>
                                    <td><span class="badge-c">Wait — do NOT enter here</span></td>
                                </tr>
                                <tr>
                                    <td><strong style="color:#00ff88;">Displacement</strong></td>
                                    <td>Extended Range Candle breaks opposite structure (CHoCH)</td>
                                    <td>Institutional execution begins — large position fills</td>
                                    <td>"Too late to enter — missed the move"</td>
                                    <td><span class="badge-aaa">Mark LTF FVG / OB for entry</span></td>
                                </tr>
                                <tr>
                                    <td><strong style="color:#00ff88;">Distribution</strong></td>
                                    <td>True directional move to the opposing PD array target</td>
                                    <td>Institutions riding position to profit-taking zone</td>
                                    <td>Entered too late, chasing — poor RR</td>
                                    <td><span class="badge-aaa">Riding 1:5+ RR with runner</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4. OPERATOR MINDSET -->
                <div class="content-section">
                    <h3><i class='bx bx-brain'></i> 4. The Operator Mindset — The Psychological Architecture of a Professional</h3>
                    <p>The single largest determinant of trading profitability is not strategy — it is mindset. Every losing retail trader has access to the same chart as a successful institutional operator. The difference is <strong>how</strong> they interpret what they see, and <strong>what decisions</strong> they allow themselves to make.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left:4px solid #ff3333;">
                            <h4 style="color:#ff3333;margin-bottom:10px;">❌ Retail Gambler Psychology</h4>
                            <ul style="font-size:12px;color:#888;list-style:none;padding:0;line-height:2.0;">
                                <li>❌ Enters trades out of FOMO or boredom</li>
                                <li>❌ Moves stop-loss further away "to give it room"</li>
                                <li>❌ Revenge trades immediately after a loss</li>
                                <li>❌ Doubles position size after a loss to "recover"</li>
                                <li>❌ Takes profits at 1:1 and holds losers to breakeven</li>
                                <li>❌ No journaling — decisions based on emotion</li>
                                <li>❌ Changes strategy every week after 2 losers</li>
                            </ul>
                        </div>
                        <div class="example-box" style="border-left:4px solid #00ff88;">
                            <h4 style="color:#00ff88;margin-bottom:10px;">✅ Institutional Operator Psychology</h4>
                            <ul style="font-size:12px;color:#ccc;list-style:none;padding:0;line-height:2.0;">
                                <li>✅ Only trades pre-defined, high-confluence setups</li>
                                <li>✅ Stop-loss is set <em>before</em> entry — never moved wider</li>
                                <li>✅ Treats a loss as a statistical business expense</li>
                                <li>✅ Risk per trade is always fixed at 1% of account</li>
                                <li>✅ Lets winners run with a trailing structural stop</li>
                                <li>✅ Journals every trade — decisions based on data</li>
                                <li>✅ Strategy consistency for minimum 100 sample trades</li>
                            </ul>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top:20px;">
                        <h4>🔑 The 3 Pillars of Consistent Profitability</h4>
                        <div class="grid-2">
                            <div class="sd-step-card">
                                <div class="sd-step-num">1</div>
                                <strong style="color:var(--vip-gold);font-size:14px;">Process Over Outcome</strong>
                                <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">A professional judges a trade on whether they followed their process — not whether it was a winner. A perfectly-executed losing trade is a success. A winning trade taken outside the rules is a failure.</p>
                            </div>
                            <div class="sd-step-card">
                                <div class="sd-step-num">2</div>
                                <strong style="color:var(--vip-gold);font-size:14px;">Probability &amp; Edge Over Certainty</strong>
                                <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">No setup has 100% win rate. Your edge is a statistical advantage over hundreds of trades. Any single trade is a coin flip. Your job is to execute your edge consistently and let the math compound.</p>
                            </div>
                        </div>
                        <div class="sd-step-card" style="margin-top:15px;border-left:4px solid #00ff88;">
                            <div class="sd-step-num" style="background:#00ff88;">3</div>
                            <strong style="color:#00ff88;font-size:14px;">Capital Preservation Is The Primary Job</strong>
                            <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">Profitable trading is not about making as much money as possible — it is about <em>not losing</em> your account. A 50% drawdown requires a 100% gain to recover. Keep drawdown below 10% monthly maximum. The traders who stay in the game longest win the most.</p>
                        </div>
                    </div>
                </div>

                <!-- 5. THE 90% LOSS ROOT CAUSE -->
                <div class="content-section">
                    <h3><i class='bx bx-error-circle'></i> 5. The Root Cause of the 90% Loss Rate</h3>
                    <p>Retail trading education is systematically designed — whether intentionally or structurally — to produce losing traders. The tools taught (indicators, patterns, fundamentals) all share one fatal flaw: <strong>they are lagging, publicly available, and they create predictable order clustering</strong> that institutional algorithms exploit.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr><th>Retail Tool</th><th>Why It Creates Losses</th><th>How Institutions Exploit It</th><th>Edge</th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Support &amp; Resistance Lines</strong></td>
                                    <td>Every retail trader draws the same line → identical stop cluster</td>
                                    <td>IPDA sweeps the line to harvest stops before reversing</td>
                                    <td><span class="badge-c">Retail Loses</span></td>
                                </tr>
                                <tr>
                                    <td><strong>RSI Overbought / Oversold</strong></td>
                                    <td>Lagging by definition. OB can stay OB for 200 candles in a trend</td>
                                    <td>Institutions push price further OB/OS to liquidate retail shorts/longs</td>
                                    <td><span class="badge-c">Retail Loses</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Chart Patterns (H&amp;S, Triangles)</strong></td>
                                    <td>Too well-known — become self-fulfilling until they're used against retail</td>
                                    <td>Fake pattern completion to sweep breakout traders</td>
                                    <td><span class="badge-c">Retail Loses</span></td>
                                </tr>
                                <tr>
                                    <td><strong>SMC: Supply &amp; Demand Zones</strong></td>
                                    <td>Origin of true imbalance — unfilled institutional limit orders</td>
                                    <td>Institutions <em>are</em> the orders returning to be filled</td>
                                    <td><span class="badge-aaa">Edge: Trade WITH</span></td>
                                </tr>
                                <tr>
                                    <td><strong>SMC: Liquidity Engineering</strong></td>
                                    <td>Understanding where stop-loss clusters rest and why price targets them</td>
                                    <td>Institutions program IPDA to seek and consume these pools</td>
                                    <td><span class="badge-aaa">Edge: Predict sweeps</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="example-box" style="border-left:4px solid var(--vip-gold);margin-top:20px;">
                        <p style="font-size:15px;text-align:center;color:var(--vip-gold);font-style:italic;line-height:1.6;">"If every retail trader is looking at the same indicator, the same support level, and placing their stop in the same place — they have collectively created a predictable, exploitable liquidity pool. The institution's algorithm will target that pool every single time."</p>
                        <p style="text-align:center;font-size:12px;color:#666;margin-top:10px;">— EdgeGrid Traders Capital: Institutional Operator Thesis</p>
                    </div>
                </div>

                <!-- MODULE 1 VIDEO -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 1 Masterclass: Institutional Forex Architecture &amp; The Operator Mindset</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/sQBTswIavnw?rel=0&modestbranding=1"
                            title="Institutional Forex Architecture"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                </div>

                <div class="content-nav">
                    <button class="nav-btn" disabled><i class='bx bx-left-arrow-alt'></i> Previous</button>
                    <button class="nav-btn primary" onclick="showModule(2)">Module 2: Market Structure <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>

"""

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 5 — full deep replacement
# ─────────────────────────────────────────────────────────────────────────────
NEW_MODULE_5 = """            <div class="module-content-pane" id="module-5">
                <div class="module-hero">
                    <span class="module-number">Precision Trigger Mechanics</span>
                    <h1>Module 5: Entry Models &amp; Execution Framework</h1>
                    <p>The exact institutional playbook: the two master entry blueprints, session kill zones, LTF alignment protocols, risk entry vs confirmation entry mechanics, and the comprehensive trade management system that protects capital and maximises runners.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 75%;"></div>
                    </div>
                </div>

                <!-- 1. THE 2 MASTER ENTRY BLUEPRINTS -->
                <div class="content-section">
                    <h3><i class='bx bx-bullseye'></i> 1. The 2 Master Execution Blueprints</h3>
                    <p>Professional trading eliminates subjectivity at the execution level. In the EdgeGrid methodology, you trade exactly <strong>two entry models</strong>. If a setup does not qualify as one of these two, you do not trade it — period. This rule alone eliminates 80% of losing trades caused by emotional, impulsive, or low-probability entries.</p>

                    <!-- Entry Model SVG -->
                    <div class="illustration-container">
                        <div style="background:#080808;border:1px solid #222;border-radius:16px;padding:24px;overflow-x:auto;">
                            <svg viewBox="0 0 740 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;min-width:580px;height:auto;display:block;">
                                <defs>
                                    <marker id="aGm5" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#00ff88"/></marker>
                                    <marker id="aRm5" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#ff4444"/></marker>
                                    <marker id="aYm5" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" fill="#D6FF00"/></marker>
                                </defs>

                                <!-- MODEL 1 LEFT SIDE -->
                                <text x="185" y="18" fill="#D6FF00" font-size="13" font-weight="700" text-anchor="middle">MODEL 1: SWEEP &amp; SHIFT (Reversal)</text>
                                <text x="185" y="32" fill="#888" font-size="10" text-anchor="middle">Highest Win Rate · HTF POI Required</text>

                                <!-- HTF Supply zone box -->
                                <rect x="20" y="44" width="330" height="30" rx="4" fill="rgba(255,68,68,0.1)" stroke="#ff4444" stroke-dasharray="4,3"/>
                                <text x="185" y="64" fill="#ff4444" font-size="11" font-weight="700" text-anchor="middle">HTF SUPPLY ZONE (4H / Daily)</text>

                                <!-- Price action M1 left -->
                                <!-- Price rises into zone -->
                                <line x1="45" y1="220" x2="45" y2="175" stroke="#00ff88" stroke-width="2"/>
                                <rect x="38" y="178" width="14" height="40" rx="2" fill="#00ff88" opacity="0.7"/>
                                <line x1="75" y1="200" x2="75" y2="155" stroke="#00ff88" stroke-width="2"/>
                                <rect x="68" y="158" width="14" height="40" rx="2" fill="#00ff88" opacity="0.8"/>
                                <line x1="105" y1="180" x2="105" y2="118" stroke="#00ff88" stroke-width="2"/>
                                <rect x="98" y="120" width="14" height="58" rx="2" fill="#00ff88"/>

                                <!-- Sweep candle -->
                                <line x1="140" y1="200" x2="140" y2="38" stroke="#ff4444" stroke-width="2.5"/>
                                <rect x="132" y="48" width="16" height="30" rx="2" fill="#ff4444"/>
                                <text x="140" y="258" fill="#ff4444" font-size="9" font-weight="700" text-anchor="middle">LIQUIDITY SWEEP</text>
                                <text x="140" y="268" fill="#888" font-size="8" text-anchor="middle">(stop cascade above highs)</text>

                                <!-- CHoCH displacement -->
                                <line x1="175" y1="90" x2="175" y2="195" stroke="#00ff88" stroke-width="3"/>
                                <rect x="167" y="125" width="16" height="68" rx="2" fill="#00ff88"/>
                                <text x="162" y="112" fill="#00ff88" font-size="9" font-weight="700">CHoCH</text>

                                <!-- Entry zone -->
                                <rect x="188" y="155" width="90" height="25" rx="4" fill="rgba(214,255,0,0.1)" stroke="#D6FF00" stroke-dasharray="3,2"/>
                                <text x="233" y="169" fill="#D6FF00" font-size="10" font-weight="700" text-anchor="middle">LTF OB / FVG</text>

                                <!-- Entry arrow -->
                                <path d="M 240 178 L 240 215" stroke="#D6FF00" stroke-width="2" fill="none" marker-end="url(#aYm5)"/>
                                <text x="258" y="210" fill="#D6FF00" font-size="10" font-weight="700">ENTRY</text>

                                <!-- SL line -->
                                <line x1="190" y1="240" x2="330" y2="240" stroke="#ff4444" stroke-width="1" stroke-dasharray="3,2"/>
                                <text x="335" y="244" fill="#ff4444" font-size="9">SL</text>

                                <!-- TP arrow -->
                                <path d="M 295 200 L 345 80" stroke="#00ff88" stroke-width="1.5" fill="none" marker-end="url(#aGm5)"/>
                                <text x="348" y="90" fill="#00ff88" font-size="10">TP</text>

                                <!-- Divider -->
                                <line x1="370" y1="15" x2="370" y2="275" stroke="#333" stroke-width="1.5"/>

                                <!-- MODEL 2 RIGHT SIDE -->
                                <text x="555" y="18" fill="#00ff88" font-size="13" font-weight="700" text-anchor="middle">MODEL 2: TREND CONTINUATION (BOS)</text>
                                <text x="555" y="32" fill="#888" font-size="10" text-anchor="middle">Trend Alignment Required · 15M Structure</text>

                                <!-- Uptrend candles -->
                                <line x1="390" y1="250" x2="390" y2="200" stroke="#00ff88" stroke-width="2"/>
                                <rect x="383" y="205" width="14" height="43" rx="2" fill="#00ff88" opacity="0.7"/>
                                <line x1="420" y1="225" x2="420" y2="175" stroke="#00ff88" stroke-width="2"/>
                                <rect x="413" y="178" width="14" height="45" rx="2" fill="#00ff88" opacity="0.8"/>

                                <!-- BOS line -->
                                <line x1="380" y1="200" x2="460" y2="200" stroke="#D6FF00" stroke-dasharray="4,2" stroke-width="1.5"/>
                                <text x="385" y="195" fill="#D6FF00" font-size="9" font-weight="700">BOS (15M)</text>

                                <!-- Pullback -->
                                <line x1="450" y1="160" x2="450" y2="235" stroke="#ff4444" stroke-width="2"/>
                                <rect x="443" y="190" width="14" height="44" rx="2" fill="#ff4444"/>
                                <line x1="480" y1="175" x2="480" y2="218" stroke="#ff4444" stroke-width="1.5"/>
                                <rect x="473" y="190" width="14" height="26" rx="2" fill="#ff4444" opacity="0.7"/>

                                <!-- Continuation OB zone -->
                                <rect x="490" y="188" width="90" height="28" rx="4" fill="rgba(0,255,136,0.1)" stroke="#00ff88" stroke-dasharray="3,2"/>
                                <text x="535" y="202" fill="#00ff88" font-size="10" font-weight="700" text-anchor="middle">CONTINUATION OB</text>
                                <text x="535" y="212" fill="#888" font-size="8" text-anchor="middle">50%+ into discount</text>

                                <!-- Entry and TP -->
                                <path d="M 535 185 L 535 155" stroke="#D6FF00" stroke-width="2" fill="none" marker-end="url(#aYm5)"/>
                                <text x="548" y="160" fill="#D6FF00" font-size="10" font-weight="700">ENTRY</text>
                                <path d="M 600 180 L 680 80" stroke="#00ff88" stroke-width="1.5" fill="none" marker-end="url(#aGm5)"/>
                                <text x="682" y="78" fill="#00ff88" font-size="10">TP</text>

                                <!-- SL -->
                                <line x1="490" y1="240" x2="620" y2="240" stroke="#ff4444" stroke-width="1" stroke-dasharray="3,2"/>
                                <text x="625" y="244" fill="#ff4444" font-size="9">SL</text>
                            </svg>
                        </div>
                        <p style="font-size:11px;color:#555;margin-top:10px;text-align:center;">The two master entry blueprints: Model 1 (Sweep &amp; Shift) is for high-timeframe POI reversals. Model 2 (BOS Retest) is for trend continuation entries.</p>
                    </div>

                    <div class="grid-2" style="margin-top:20px;">
                        <div class="example-box" style="border-left:4px solid var(--vip-gold);">
                            <h4 style="color:var(--vip-gold);margin-bottom:8px;">Model 1: The Sweep &amp; Shift (Reversal)</h4>
                            <p style="font-size:13px;line-height:1.6;margin-bottom:10px;">Highest win-rate setup. Used when price reaches a Higher Timeframe (4H/Daily) Supply or Demand POI. Requires a completed liquidity sweep followed by a displacement CHoCH.</p>
                            <ol style="font-size:12px;color:var(--vip-text);line-height:1.9;padding-left:18px;">
                                <li><strong>HTF Tap:</strong> Price taps into your marked 4H or Daily Supply / Demand zone.</li>
                                <li><strong>Liquidity Sweep:</strong> Drop to M5 or M1. Price makes a sharp fake move, sweeping retail stops.</li>
                                <li><strong>Displacement (CHoCH):</strong> Price violently snaps back with an Extended Range Candle, breaking the prior opposing swing, leaving a Fair Value Gap.</li>
                                <li><strong>LTF Entry:</strong> Place limit order at the proximal edge of the new LTF Order Block or inside the FVG.</li>
                                <li><strong>Stop Loss:</strong> 2–4 pips beyond the extreme of the sweep wick.</li>
                            </ol>
                        </div>
                        <div class="example-box" style="border-left:4px solid #00ff88;">
                            <h4 style="color:#00ff88;margin-bottom:8px;">Model 2: Trend Continuation (BOS Retest)</h4>
                            <p style="font-size:13px;line-height:1.6;margin-bottom:10px;">Used to enter a running trend during active London or NY Kill Zone. Requires a clean 15M structure break followed by a discount/premium pullback to a continuation OB.</p>
                            <ol style="font-size:12px;color:var(--vip-text);line-height:1.9;padding-left:18px;">
                                <li><strong>15M BOS:</strong> Aggressive, clean break of a significant 15M swing high (bull) or swing low (bear) with an ERC.</li>
                                <li><strong>Pullback:</strong> Wait for price to retrace ≥50% into the displacement leg (Discount for buys, Premium for sells).</li>
                                <li><strong>Continuation OB:</strong> Locate the unmitigated continuation Order Block or FVG inside the discount zone.</li>
                                <li><strong>Entry:</strong> Limit order at proximal edge. Target: next 4H swing extreme.</li>
                                <li><strong>Stop Loss:</strong> Below the distal edge of the OB + 2–3 pip buffer.</li>
                            </ol>
                        </div>
                    </div>

                    <!-- Entry Type Comparison -->
                    <div class="key-takeaways" style="margin-top:20px;">
                        <h4>⚡ Risk Entry vs. Confirmation Entry — Choosing Your Precision Level</h4>
                        <div class="sd-table-container" style="margin-top:10px;">
                            <table class="sd-table">
                                <thead>
                                    <tr><th>Entry Type</th><th>When to Use</th><th>Average RR</th><th>Win Rate</th><th>Risk Level</th><th>EdgeGrid Rating</th></tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Risk Entry (LTF OB)</strong></td>
                                        <td>HTF POI tap + visible CHoCH on M1/M5</td>
                                        <td>1:5 – 1:10+</td>
                                        <td>~45–55%</td>
                                        <td>Higher risk per trade</td>
                                        <td><span class="badge-aaa">Master Level</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Confirmation Entry (FVG Retest)</strong></td>
                                        <td>Wait for price to return to displacement FVG after CHoCH</td>
                                        <td>1:3 – 1:5</td>
                                        <td>~60–70%</td>
                                        <td>Lower risk per trade</td>
                                        <td><span class="badge-b">Recommended for Learners</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Market Order Entry</strong></td>
                                        <td>Never — chasing price</td>
                                        <td>&lt;1:1</td>
                                        <td>&lt;40%</td>
                                        <td>Extremely high</td>
                                        <td><span class="badge-c">Prohibited</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- 2. SESSION KILL ZONES -->
                <div class="content-section">
                    <h3><i class='bx bx-time'></i> 2. The Power of Time: Session Kill Zones &amp; Algorithmic Windows</h3>
                    <p>Every entry model becomes <strong>exponentially more powerful</strong> when executed inside the correct time window. Algorithms are programmed to release institutional volume during specific windows when Tier-1 interbank desks in London and New York overlap. Trading outside these kill zones means fighting low liquidity, erratic spreads, and manipulated price action with no follow-through.</p>

                    <!-- Session Timeline SVG -->
                    <div class="illustration-container">
                        <div style="background:#080808;border:1px solid #222;border-radius:16px;padding:24px;overflow-x:auto;">
                            <svg viewBox="0 0 720 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;min-width:580px;height:auto;display:block;">
                                <!-- Timeline bar -->
                                <rect x="20" y="60" width="680" height="30" rx="4" fill="#111"/>

                                <!-- Asian: 00:00 - 06:00 = 0-170px -->
                                <rect x="20" y="60" width="170" height="30" rx="4" fill="rgba(100,100,100,0.3)" stroke="#555"/>
                                <text x="105" y="80" fill="#888" font-size="10" font-weight="700" text-anchor="middle">ASIAN</text>
                                <text x="105" y="92" fill="#666" font-size="9" text-anchor="middle">00:00 – 06:00 UTC</text>

                                <!-- Pre-London: 06:00-07:00 = 170-198px -->
                                <rect x="190" y="60" width="28" height="30" fill="rgba(200,200,0,0.1)" stroke="#555" stroke-dasharray="2"/>

                                <!-- London Kill Zone: 07:00 - 10:00 = 198-283px -->
                                <rect x="218" y="50" width="85" height="50" rx="4" fill="rgba(214,255,0,0.12)" stroke="#D6FF00" stroke-width="2"/>
                                <text x="260" y="72" fill="#D6FF00" font-size="11" font-weight="700" text-anchor="middle">LONDON KZ</text>
                                <text x="260" y="84" fill="#999" font-size="9" text-anchor="middle">07:00–10:00</text>
                                <text x="260" y="96" fill="#D6FF00" font-size="9" text-anchor="middle">⭐ HIGH PRIORITY</text>

                                <!-- Mid-session -->
                                <rect x="303" y="60" width="85" height="30" rx="4" fill="rgba(255,255,255,0.02)" stroke="#333"/>
                                <text x="345" y="80" fill="#555" font-size="10" text-anchor="middle">Pre-NY</text>

                                <!-- NY Kill Zone: 12:00 - 15:00 -->
                                <rect x="388" y="50" width="85" height="50" rx="4" fill="rgba(0,255,136,0.1)" stroke="#00ff88" stroke-width="2"/>
                                <text x="430" y="72" fill="#00ff88" font-size="11" font-weight="700" text-anchor="middle">NEW YORK KZ</text>
                                <text x="430" y="84" fill="#999" font-size="9" text-anchor="middle">12:00–15:00</text>
                                <text x="430" y="96" fill="#00ff88" font-size="9" text-anchor="middle">⭐ HIGH PRIORITY</text>

                                <!-- Late NY -->
                                <rect x="473" y="60" width="100" height="30" rx="4" fill="rgba(255,50,50,0.06)" stroke="#ff3333" stroke-dasharray="3,2"/>
                                <text x="523" y="79" fill="#ff3333" font-size="10" font-weight="700" text-anchor="middle">DANGER ZONE</text>
                                <text x="523" y="91" fill="#cc3333" font-size="9" text-anchor="middle">19:00–23:00 UTC</text>

                                <!-- Rollover -->
                                <rect x="573" y="60" width="127" height="30" rx="4" fill="rgba(80,80,80,0.2)" stroke="#444"/>
                                <text x="636" y="80" fill="#777" font-size="9" text-anchor="middle">ROLLOVER / CLOSE</text>

                                <!-- Time markers -->
                                <text x="20" y="125" fill="#555" font-size="9">00:00</text>
                                <text x="188" y="125" fill="#555" font-size="9">06:00</text>
                                <text x="218" y="125" fill="#D6FF00" font-size="9">07:00</text>
                                <text x="296" y="125" fill="#D6FF00" font-size="9">10:00</text>
                                <text x="388" y="125" fill="#00ff88" font-size="9">12:00</text>
                                <text x="468" y="125" fill="#00ff88" font-size="9">15:00</text>
                                <text x="570" y="125" fill="#ff3333" font-size="9">19:00</text>
                                <text x="670" y="125" fill="#555" font-size="9">24:00</text>
                            </svg>
                        </div>
                        <p style="font-size:11px;color:#555;margin-top:10px;text-align:center;">Session Kill Zone Timeline (UTC). All EdgeGrid entries must occur inside the London KZ (07:00–10:00) or NY KZ (12:00–15:00) windows.</p>
                    </div>

                    <div class="sd-table-container" style="margin-top:20px;">
                        <table class="sd-table">
                            <thead>
                                <tr><th>Session</th><th>Time (UTC)</th><th>Market Characteristic</th><th>Judas Swing?</th><th>Optimal EdgeGrid Action</th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Asian Session</strong></td>
                                    <td>00:00 – 06:00</td>
                                    <td>Tight consolidation. Low volume. Liquidity builds on both sides of the range.</td>
                                    <td><span class="badge-b">Sometimes</span></td>
                                    <td><strong>Hands off.</strong> Mark the Asian High &amp; Low as target liquidity pools for London.</td>
                                </tr>
                                <tr>
                                    <td><strong>London Kill Zone</strong></td>
                                    <td>07:00 – 10:00 ⭐</td>
                                    <td>Peak European volume. Creates the "Judas Swing" — a false sweep of the Asian range before the true London trend begins.</td>
                                    <td><span class="badge-aaa">Yes — ~85% of days</span></td>
                                    <td><strong>Prime hunting ground.</strong> Watch for Model 1 sweep of the Asian range, then ride the displacement toward NY.</td>
                                </tr>
                                <tr>
                                    <td><strong>New York Kill Zone</strong></td>
                                    <td>12:00 – 15:00 ⭐</td>
                                    <td>Peak global volume. US economic data releases (CPI, NFP, FOMC). Largest volume bars of the day.</td>
                                    <td><span class="badge-b">On news days</span></td>
                                    <td><strong>Continuation or NY Reversal.</strong> Ride confirmed London trend via Model 2 OR hunt NY reversal if London was extended.</td>
                                </tr>
                                <tr>
                                    <td><strong>NY Afternoon / Late</strong></td>
                                    <td>15:00 – 19:00</td>
                                    <td>Institutional desks partially closing. Thin volume. Erratic movement.</td>
                                    <td><span class="badge-c">Avoid</span></td>
                                    <td><strong>Manage open trades only.</strong> No new entries. Move stop to break-even on any runner.</td>
                                </tr>
                                <tr>
                                    <td><strong>Rollover / Danger</strong></td>
                                    <td>19:00 – 23:00</td>
                                    <td>Spreads widen 5x–10x. Algos generate noise patterns with no institutional direction. Stop hunting common.</td>
                                    <td><span class="badge-c">High frequency</span></td>
                                    <td><strong>All positions flat or protected.</strong> Never enter. This window destroys retail accounts.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 3. LTF ALIGNMENT FRAMEWORK -->
                <div class="content-section">
                    <h3><i class='bx bx-layer'></i> 3. The Multi-Timeframe Alignment Protocol</h3>
                    <p>The most powerful entries require all three timeframe layers to be in agreement. If any layer disagrees, the setup does not qualify and must be skipped. This is the institutional concept of <strong>"Top-Down Confluence"</strong> — working from the largest timeframe narrative down to the M1 trigger.</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num" style="background:var(--vip-gold);color:#000;">1</div>
                            <strong style="color:var(--vip-gold);font-size:14px;">Layer 1: HTF Narrative (Daily / Weekly)</strong>
                            <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">Determine the macro directional bias. Is price in a bullish or bearish market structure? What is the nearest HTF Supply or Demand zone? Has a significant liquidity pool been created? This layer controls the overall trade direction.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">2</div>
                            <strong style="color:var(--vip-gold);font-size:14px;">Layer 2: Execution Timeframe (1H / 15M)</strong>
                            <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">Confirm the intermediate structure supports the HTF bias. Is the 15M in a BOS sequence in the same direction as the Daily? Has price returned to a 15M discount (for buys) or premium (for sells)? This layer confirms the setup type.</p>
                        </div>
                    </div>
                    <div class="sd-step-card" style="margin-top:15px;border-left:4px solid #00ff88;">
                        <div class="sd-step-num" style="background:#00ff88;">3</div>
                        <strong style="color:#00ff88;font-size:14px;">Layer 3: Trigger Timeframe (M5 / M1)</strong>
                        <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">The precision entry layer. Drop to M5 or M1 to find the specific order block or FVG to enter. The CHoCH must be visible on this timeframe. Your stop loss is placed using M1 candle wicks only — never M15 or H1 structure. This ensures maximum Risk-to-Reward ratios of 1:5 to 1:10+.</p>
                    </div>

                    <div class="sd-table-container" style="margin-top:20px;">
                        <table class="sd-table">
                            <thead>
                                <tr><th>Timeframe</th><th>Role</th><th>Key Question to Ask</th><th>Must See Before Entry</th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Weekly / Daily</strong></td>
                                    <td>Macro narrative</td>
                                    <td>What is the overall directional bias? Where is the next HTF POI?</td>
                                    <td>Identifiable HTF Supply or Demand zone within reach</td>
                                </tr>
                                <tr>
                                    <td><strong>4H / 1H</strong></td>
                                    <td>Intermediate structure</td>
                                    <td>Has a BOS occurred in the direction of the Daily? Is price pulling back into a valid zone?</td>
                                    <td>15M BOS in same direction as Daily bias</td>
                                </tr>
                                <tr>
                                    <td><strong>15M</strong></td>
                                    <td>Entry structure</td>
                                    <td>Has price swept liquidity and displaced? Is there a fresh CHoCH?</td>
                                    <td>Liquidity sweep + CHoCH displacement candle</td>
                                </tr>
                                <tr>
                                    <td><strong>M5 / M1</strong></td>
                                    <td>Precision trigger</td>
                                    <td>Where is the exact Order Block or FVG to place my limit order?</td>
                                    <td>Clear LTF OB or FVG at proximal level; stop set to M1 wick</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4. TRADE MANAGEMENT -->
                <div class="content-section">
                    <h3><i class='bx bx-shield-quarter'></i> 4. The 3-Step Trade Management &amp; Capital Protection Blueprint</h3>
                    <p>Entries determine <em>when</em> you get into a trade. Trade management determines <em>whether you keep the money</em>. Poor trade management is the #1 reason profitable setups result in net account losses. Follow this three-step protocol <strong>on every position without exception</strong>.</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num">1</div>
                            <strong style="color:var(--vip-gold);font-size:14px;">The Spread Buffer Rule (SL Placement)</strong>
                            <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">Never set your stop loss exactly on a wick or candle close. Always add a <strong>2–5 pip buffer</strong> beyond the distal extreme. During London Open, Tier-1 brokers temporarily widen spreads by 1–3 pips specifically to hit exactly-placed stops. The buffer eliminates this threat on 80% of trades.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">2</div>
                            <strong style="color:var(--vip-gold);font-size:14px;">Partial Profit at 1:3 RR + Move to Break-Even</strong>
                            <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">When price hits 1:3 Risk-to-Reward, bank <strong>50% of the position</strong> and immediately move your stop loss to <strong>break-even (entry price)</strong>. The trade is now 100% risk-free. You have locked in a gain and your runner costs you nothing. This one rule removes emotional attachment from the remaining position.</p>
                        </div>
                    </div>
                    <div class="sd-step-card" style="margin-top:15px;border-left:4px solid #00ff88;">
                        <div class="sd-step-num" style="background:#00ff88;">3</div>
                        <strong style="color:#00ff88;font-size:14px;">Trail Runner Behind Structural Breaks</strong>
                        <p style="font-size:13px;color:var(--vip-text-muted);margin-top:6px;">Let the remaining 50% volume run toward your major HTF target. Only trail your stop loss behind <em>confirmed new swing points that successfully broke structure</em>. Never trail too tightly — normal pullbacks of 30–50% of the prior leg are routine and healthy in trending markets. Premature trailing is the number one cause of cutting winning trades short.</p>
                    </div>

                    <!-- R-Multiple Scorecard -->
                    <div class="key-takeaways" style="margin-top:20px;">
                        <h4>📊 Expected Value Scorecard — The EdgeGrid Performance Standard</h4>
                        <div class="sd-table-container" style="margin-top:10px;">
                            <table class="sd-table">
                                <thead>
                                    <tr><th>Metric</th><th>Minimum Standard</th><th>Good</th><th>Elite</th></tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Win Rate</strong></td>
                                        <td>40%</td>
                                        <td><span class="badge-b">50–60%</span></td>
                                        <td><span class="badge-aaa">65%+</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Average RR</strong></td>
                                        <td>1:2</td>
                                        <td><span class="badge-b">1:3 – 1:4</span></td>
                                        <td><span class="badge-aaa">1:5 – 1:8+</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Profit Factor</strong></td>
                                        <td>&gt;1.2</td>
                                        <td><span class="badge-b">1.5 – 2.0</span></td>
                                        <td><span class="badge-aaa">2.5+</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Max Monthly Drawdown</strong></td>
                                        <td>&lt;10%</td>
                                        <td><span class="badge-b">&lt;6%</span></td>
                                        <td><span class="badge-aaa">&lt;4%</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Consecutive Losses Rule</strong></td>
                                        <td>Stop after 3 in a row</td>
                                        <td><span class="badge-b">Review journal, resume next session</span></td>
                                        <td><span class="badge-aaa">Algorithmic consistency — no hesitation</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- 5. PRE-FLIGHT CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-list-check'></i> 5. The 60-Second Pre-Flight Execution Checklist</h3>
                    <p>Before pressing the trigger on your terminal, verify all 5 checklist items. If any item cannot be checked, the trade is <strong>invalid</strong> — do not enter. This is not optional. Professional traders follow this checklist on every single trade, every single day.</p>

                    <div class="example-box" style="background:rgba(0,0,0,0.4);border:1px solid var(--vip-gold);">
                        <ul style="font-size:13px;color:#fff;line-height:2.5;list-style:none;padding-left:0;">
                            <li><i class='bx bx-check-circle' style="color:var(--vip-gold);"></i> <strong>1. Time Check:</strong> Am I inside London Open (07:00–10:00 UTC) or NY Open (12:00–15:00 UTC)?</li>
                            <li><i class='bx bx-check-circle' style="color:var(--vip-gold);"></i> <strong>2. HTF Bias:</strong> Does this trade align with the Daily / 4H directional narrative?</li>
                            <li><i class='bx bx-check-circle' style="color:var(--vip-gold);"></i> <strong>3. Liquidity Sweep:</strong> Has resting retail liquidity (equal highs/lows, prior wick) been consumed before this entry?</li>
                            <li><i class='bx bx-check-circle' style="color:var(--vip-gold);"></i> <strong>4. Structural Shift:</strong> Did price displace with a clear CHoCH leaving an FVG on the trigger timeframe?</li>
                            <li><i class='bx bx-check-circle' style="color:var(--vip-gold);"></i> <strong>5. Risk &amp; Runway:</strong> Is my lot size set to risk maximum 1% of account? Is there a clean 1:3+ path to the next opposing PD array?</li>
                        </ul>
                        <div style="margin-top:15px;padding:12px;background:rgba(214,255,0,0.06);border-radius:8px;font-size:12px;color:var(--vip-gold);text-align:center;">
                            <strong>All 5 checked = Green light. Any item missing = No trade. No exceptions.</strong>
                        </div>
                    </div>
                </div>

                <!-- MODULE 5 VIDEO -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 5 Masterclass: SMC Entry Models &amp; Execution Blueprint</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/FmrkqxEmWxM?rel=0&modestbranding=1"
                            title="SMC Entry Models &amp; Execution"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                </div>

                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(4)"><i class='bx bx-left-arrow-alt'></i> Previous: Liquidity &amp; OBs</button>
                    <button class="nav-btn primary" onclick="showModule(6)">Next: Fundamental Analysis <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>

"""

# ─────────────────────────────────────────────────────────────────────────────
# Replace Module 1 in the HTML
# ─────────────────────────────────────────────────────────────────────────────
M1_START_TAG = '            <div class="module-content-pane active" id="module-1">'
M1_END_TAG   = '            <!-- MODULE 2 -->'

m1_start = html.find(M1_START_TAG)
m1_end   = html.find(M1_END_TAG)

if m1_start == -1 or m1_end == -1:
    print("ERROR: Could not find Module 1 boundaries")
    print(f"  M1_START found: {m1_start != -1}")
    print(f"  M1_END found:   {m1_end != -1}")
    exit(1)

html = html[:m1_start] + NEW_MODULE_1 + '\n' + html[m1_end:]
print(f"✓ Module 1 replaced ({m1_end - m1_start} chars → {len(NEW_MODULE_1)} chars)")

# ─────────────────────────────────────────────────────────────────────────────
# Replace Module 5 in the HTML
# ─────────────────────────────────────────────────────────────────────────────
M5_START_TAG = '            <div class="module-content-pane" id="module-5">'
M5_END_TAG   = '            <!-- MODULE 6 -->'

m5_start = html.find(M5_START_TAG)
m5_end   = html.find(M5_END_TAG)

if m5_start == -1 or m5_end == -1:
    print("ERROR: Could not find Module 5 boundaries")
    print(f"  M5_START found: {m5_start != -1}")
    print(f"  M5_END found:   {m5_end != -1}")
    exit(1)

html = html[:m5_start] + NEW_MODULE_5 + '\n' + html[m5_end:]
print(f"✓ Module 5 replaced ({m5_end - m5_start} chars → {len(NEW_MODULE_5)} chars)")

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
with open('VIPmembers.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ VIPmembers.html saved — total {len(html):,} chars / {len(html.splitlines()):,} lines")
