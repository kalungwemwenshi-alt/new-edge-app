# modules_part2.py
# Comprehensive content for Module 4 & Module 5

MODULE_4 = """            <!-- MODULE 4 -->
            <div class="module-content-pane" id="module-4">
                <div class="module-hero">
                    <span class="module-number">The Footprints of Smart Money</span>
                    <h1>Module 4: Liquidity Engineering, Order Blocks & Imbalance</h1>
                    <p>Understanding where institutional money hides, how stop-hunts are engineered, Order Block validation, Fair Value Gaps (FVG), and the 4-step raid playbook.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 50%;"></div>
                    </div>
                </div>

                <!-- 1. LIQUIDITY IN PLAIN ENGLISH -->
                <div class="content-section">
                    <h3><i class='bx bx-water'></i> 1. The Market's Fuel: BSL & SSL Liquidity Pools</h3>
                    <p>Every single transaction in the foreign exchange market requires a counterparty. If a Tier-1 institution needs to buy <strong>$800 million EUR/USD</strong>, they cannot simply hit buy at market price without causing catastrophic 30-pip upward slippage. They must engineer liquidity by driving price directly into concentrated clusters of retail sell orders: <strong>Sell-Side Liquidity (SSL)</strong>.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Buy-Side Liquidity (BSL)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Located <strong>above swing highs, double tops (equal highs), and resistance lines</strong>. Consists of retail sellers' Buy-Stop Loss orders and breakout buy orders. Institutions drive price above these highs to trigger buy orders, providing the counterparties needed for banks to <strong>SELL short</strong>.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">Sell-Side Liquidity (SSL)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Located <strong>below swing lows, double bottoms (equal lows), and support lines</strong>. Consists of retail buyers' Sell-Stop Loss orders and breakdown sell orders. Institutions drive price below these lows to trigger panic selling, providing the counterparties needed for banks to <strong>BUY long</strong>.</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The 3 Primary Liquidity Targets to Mark Daily</h4>
                        <ul>
                            <li><strong>1. Previous Day High & Low (PDH / PDL):</strong> The premier intraday liquidity targets. Over 70% of London/NY reversals occur immediately after sweeping PDH or PDL.</li>
                            <li><strong>2. Equal Highs & Equal Lows (EQH / EQL):</strong> Retail textbooks call these "Double Tops and Bottoms". To institutions, these are resting pools of purest stop liquidity.</li>
                            <li><strong>3. Trendline Liquidity Pools:</strong> Retail traders place orders along diagonal trendlines. Banks pierce trendlines like a hot knife through butter to trigger stop cascades.</li>
                        </ul>
                    </div>
                </div>

                <!-- 2. ORDER BLOCK ANATOMY & VALIDATION -->
                <div class="content-section">
                    <h3><i class='bx bx-cube'></i> 2. Order Block Anatomy & Validation Framework</h3>
                    <p>An <strong>Order Block (OB)</strong> is not simply any candlestick before a move. It is the specific price footprint where an institutional algorithm placed its contrarian orders to absorb retail liquidity immediately before unleashing violent displacement.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Bullish Order Block (+OB)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">The <strong>lowest down-close (bearish) candle</strong> prior to an explosive upward impulse that sweeps liquidity and creates an unambiguous Break of Structure (BOS) with an imbalance (FVG).</p>
                            <p style="font-size: 12px; color: var(--vip-gold); margin-top: 6px;"><strong>Execution Rule:</strong> Enter long at the open/high of the candle body with stop loss safely below the low wick.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">Bearish Order Block (-OB)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">The <strong>highest up-close (bullish) candle</strong> prior to an aggressive downward impulse that sweeps liquidity and creates an unambiguous Break of Structure (BOS) with an imbalance (FVG).</p>
                            <p style="font-size: 12px; color: var(--vip-gold); margin-top: 6px;"><strong>Execution Rule:</strong> Enter short at the open/low of the candle body with stop loss safely above the high wick.</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The 4 Non-Negotiable Order Block Validation Criteria</h4>
                        <ul>
                            <li><strong>1. Liquidity Sweep:</strong> The candidate candle must have swept prior swing liquidity (BSL or SSL) before reversing.</li>
                            <li><strong>2. Imbalance Creation (FVG):</strong> The departure move must leave a clean Fair Value Gap. Without an FVG, the move lacked true institutional velocity.</li>
                            <li><strong>3. Break of Structure (BOS):</strong> The departure must cleanly close past a valid swing point on the chart.</li>
                            <li><strong>4. Unmitigated Status:</strong> The order block must be virgin (fresh), with zero previous candle wicks having penetrated its body.</li>
                        </ul>
                    </div>
                </div>

                <!-- 3. BREAKER BLOCKS & MITIGATION BLOCKS -->
                <div class="content-section">
                    <h3><i class='bx bx-transfer-alt'></i> 3. Breaker Blocks & Mitigation Blocks</h3>
                    <p>When an order block fails to hold and is aggressively violated, it does not disappear into thin air. It transforms into an institutional <strong>Breaker Block</strong>. A Breaker Block is a failed order block that swept liquidity before failing, trapping traders on the wrong side of the market.</p>

                    <!-- SVG 3: Order Block vs Breaker Block -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Bearish Breaker Block Diagram -->
                                <!-- Swing High 1 -->
                                <polyline points="50,200 130,90 200,160 280,50 360,260 440,160 540,290" fill="none" stroke="#FFFFFF" stroke-width="2.5" />

                                <!-- Points -->
                                <circle cx="130" cy="90" r="5" fill="#aaa" />
                                <text x="130" y="75" fill="#aaa" font-size="10" text-anchor="middle">Swing High</text>

                                <circle cx="200" cy="160" r="5" fill="#aaa" />
                                <text x="200" y="180" fill="#aaa" font-size="10" text-anchor="middle">Swing Low</text>

                                <!-- Higher High (Sweep) -->
                                <circle cx="280" cy="50" r="6" fill="#ff4444" />
                                <text x="280" y="35" fill="#ff4444" font-size="11" font-weight="700" text-anchor="middle">HIGHER HIGH (SWEEPS BSL)</text>

                                <!-- Breaker Level Box across Swing Low -->
                                <rect x="180" y="145" width="300" height="30" fill="rgba(255, 68, 68, 0.15)" stroke="#ff4444" stroke-width="1.5" stroke-dasharray="3,3" rx="4" />
                                <text x="320" y="135" fill="#ff4444" font-size="11" font-weight="700">BEARISH BREAKER BLOCK</text>
                                <text x="320" y="195" fill="#888" font-size="9">Failed Demand Flipped into Institutional Supply</text>

                                <!-- Retest Point -->
                                <circle cx="440" cy="160" r="6" fill="#00ff88" />
                                <text x="440" y="140" fill="#00ff88" font-size="11" font-weight="800" text-anchor="middle">PRECISION SHORT ENTRY</text>

                                <!-- Downward Arrow -->
                                <path d="M 450 180 L 530 280" stroke="#00ff88" stroke-width="2" marker-end="url(#m4ArrowGreen)" fill="none" />
                                <text x="520" y="250" fill="#00ff88" font-size="10" font-weight="700">TARGET: SSL</text>

                                <defs>
                                    <marker id="m4ArrowGreen" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                                        <path d="M 0 0 L 8 4 L 0 8 Z" fill="#00ff88" />
                                    </marker>
                                </defs>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The Bearish Breaker Block: Price prints a Higher High that sweeps liquidity, then violently collapses through the intermediate low. That broken low flips into an institutional Breaker Block for high-probability continuation.</p>
                    </div>
                </div>

                <!-- 4. FAIR VALUE GAPS & INEFFICIENCIES -->
                <div class="content-section">
                    <h3><i class='bx bx-unite'></i> 4. Fair Value Gaps (FVG) & Consequent Encroachment</h3>
                    <p>A <strong>Fair Value Gap (FVG)</strong> represents a 3-candlestick price imbalance where aggressive one-sided order flow resulted in price delivering only buy or only sell volume. The market auction becomes inefficient, and IPDA will systematically re-deliver price back to fill the void.</p>

                    <!-- SVG 4: 3-Candle FVG Schematic -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Candle 1 (Bullish) -->
                                <line x1="200" y1="120" x2="200" y2="230" stroke="#00ff88" stroke-width="2" />
                                <rect x="188" y="140" width="24" height="70" fill="#00ff88" rx="2" />
                                <text x="200" y="255" fill="#888" font-size="11" text-anchor="middle">Candle 1</text>
                                <text x="200" y="110" fill="#aaa" font-size="9" text-anchor="middle">High of Candle 1</text>

                                <!-- Candle 2 (Large Bullish Displacement ERC) -->
                                <line x1="320" y1="30" x2="320" y2="210" stroke="#00ff88" stroke-width="2" />
                                <rect x="306" y="45" width="28" height="150" fill="#00ff88" rx="2" />
                                <text x="320" y="255" fill="#00ff88" font-size="11" font-weight="700" text-anchor="middle">Candle 2 (Displacement)</text>

                                <!-- Candle 3 (Bullish) -->
                                <line x1="440" y1="20" x2="440" y2="130" stroke="#00ff88" stroke-width="2" />
                                <rect x="428" y="35" width="24" height="70" fill="#00ff88" rx="2" />
                                <text x="440" y="255" fill="#888" font-size="11" text-anchor="middle">Candle 3</text>
                                <text x="440" y="145" fill="#aaa" font-size="9" text-anchor="middle">Low of Candle 3</text>

                                <!-- FVG Shaded Zone between Candle 1 High and Candle 3 Low -->
                                <rect x="160" y="120" width="340" height="20" fill="rgba(214, 255, 0, 0.2)" stroke="var(--vip-gold)" stroke-width="1.5" stroke-dasharray="3,3" rx="4" />
                                <text x="560" y="132" fill="var(--vip-gold)" font-size="12" font-weight="800">BULLISH FAIR VALUE GAP (FVG)</text>
                                <text x="560" y="148" fill="#aaa" font-size="9">Consequent Encroachment (50% Midpoint)</text>

                                <!-- Midpoint line CE -->
                                <line x1="160" y1="130" x2="500" y2="130" stroke="var(--vip-gold)" stroke-width="1" stroke-dasharray="2,2" />
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The 3-Candle Fair Value Gap: The void between the High of Candle 1 and the Low of Candle 3 is an unmitigated inefficiency. Consequent Encroachment (CE, 50% line) serves as the primary sniper entry level.</p>
                    </div>
                </div>

                <!-- 5. COMPARISON TABLE -->
                <div class="content-section">
                    <h3><i class='bx bx-table'></i> 5. Liquidity & Footprint Quality Matrix</h3>
                    <p>Evaluating institutional footprints based on mathematical win rate, strike rate, and R:R expectancy.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Footprint Type</th>
                                    <th>Prerequisites</th>
                                    <th>Win Rate</th>
                                    <th>Target R:R</th>
                                    <th>Execution Protocol</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Grade AAA Order Block</strong></td>
                                    <td>Swept Major Liquidity + Created FVG + BOS</td>
                                    <td>74% - 82%</td>
                                    <td>1:5 to 1:10</td>
                                    <td>Set Limit Order at Open / 50% Mean Threshold</td>
                                </tr>
                                <tr>
                                    <td><strong>Breaker Block Transition</strong></td>
                                    <td>Failed OB that swept liquidity before BOS</td>
                                    <td>70% - 78%</td>
                                    <td>1:4 to 1:8</td>
                                    <td>Direct Limit Entry on Retest of Broken Pivot</td>
                                </tr>
                                <tr>
                                    <td><strong>Fair Value Gap (FVG)</strong></td>
                                    <td>Displacement void inside discount/premium</td>
                                    <td>68% - 75%</td>
                                    <td>1:3 to 1:6</td>
                                    <td>Entry at Consequent Encroachment (50% Level)</td>
                                </tr>
                                <tr>
                                    <td><strong>Inducement Trap (Fake OB)</strong></td>
                                    <td>No liquidity sweep prior to move; mid-range</td>
                                    <td>25% - 35%</td>
                                    <td>Negative</td>
                                    <td>STAND ASIDE - Used as fuel by smart money</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 6. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 6. VIP Interactive Tool: Liquidity Sweep & Order Block Validator</h3>
                    <p>Audit any Order Block or Liquidity setup before risk execution. Compute the algorithmic probability grade and receive immediate operational guidance.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-check-shield'></i> Order Block Audit Terminal</h4>
                            <span class="badge-institutional">MODULE 4 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-water'></i> Liquidity Sweep Magnitude</label>
                                <select id="m4Sweep">
                                    <option value="30">Swept Major HTF Liquidity (PDH/PDL or EQH/EQL) (+30 Pts)</option>
                                    <option value="15">Swept Minor Asian or Session Extremes (+15 Pts)</option>
                                    <option value="0">No Liquidity Swept (Formed Inside Range) (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-rocket'></i> Displacement & FVG Creation</label>
                                <select id="m4Displacement">
                                    <option value="30">Violent Multi-Candle ERCs with Large Clean FVG (+30 Pts)</option>
                                    <option value="15">Moderate Candle Body with Small Imbalance (+15 Pts)</option>
                                    <option value="0">Sluggish Departure / Overlapping Wicks (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-git-commit'></i> Structural Impact (BOS / CHoCH)</label>
                                <select id="m4Structure">
                                    <option value="20">Broke Major Structural Swing Point with Body Close (+20 Pts)</option>
                                    <option value="10">Broke Minor Internal Pivot Only (+10 Pts)</option>
                                    <option value="0">No Structure Broken (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-recycle'></i> Mitigation History</label>
                                <select id="m4Mitigation">
                                    <option value="20">Virgin / Unmitigated (0 Previous Touches) (+20 Pts)</option>
                                    <option value="5">Tapped Once Already (+5 Pts)</option>
                                    <option value="0">Multi-Tapped 2+ Times (Hollowed Out) (0 Pts)</option>
                                </select>
                            </div>
                        </div>

                        <button class="calc-btn" onclick="validateOrderBlock()" style="margin-top: 15px;">
                            <i class='bx bx-analyse'></i> Audit Order Block Validity
                        </button>

                        <div id="m4ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">COMPUTED ORDER BLOCK SCORE</div>
                                <div id="m4GradeBadge" class="badge-aaa">GRADE AAA: INSTITUTIONAL BLOCK</div>
                            </div>
                            <div class="value" id="m4ScoreValue" style="text-align: center; font-size: 38px; margin: 15px 0;">100 / 100</div>
                            <p id="m4Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m4Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 7. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 7. The VIP Liquidity & Order Block Checklist</h3>
                    <p>Execute trades only after verifying all 7 criteria:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Sweep Verified:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never buy or sell an Order Block that failed to sweep prior liquidity. The sweep is the fuel that funds the institutional move.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">FVG Must Exist Ahead:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If there is no 3-candle Fair Value Gap immediately following the order block, the departure lacked institutional velocity.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Mean Threshold (50%) Precision:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">The 50% midpoint of the Order Block body is the institutional Mean Threshold. If price penetrates beyond 50%, the block is likely failing.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Identify Inducement (IDM):</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Look for an obvious minor pullback sitting right ahead of your Order Block. That is retail inducement designed to be swept directly into your entry.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Avoid Second Retests on OBs:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">The first test of an Order Block carries 80%+ probability. By the second or third test, resting orders are exhausted and the block will be swept.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Target External Liquidity Pools:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Exit your position right before price reaches equal highs, equal lows, or the previous day's high/low.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Breaker Invalidation Rule:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If a bullish order block gets blown through with a full candle body close, immediately switch your bias: wait for the retest from below to sell the Breaker Block.</p>
                    </div>
                </div>

                <!-- 8. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 4 Masterclass: Liquidity Engineering & Order Block Footprints</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/5Dq93fGvQk0?rel=0&modestbranding=1"
                            title="Liquidity Engineering & Order Block Footprints Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 20:15:</strong> BSL vs SSL Liquidity Mapping & Inducement (IDM) Mechanics.</li>
                            <li><strong>20:16 - 41:20:</strong> Institutional Order Block Validation: Mean Threshold & Displacement.</li>
                            <li><strong>41:21 - 59:45:</strong> Fair Value Gaps (FVGs), Consequent Encroachment & Breaker Block Transitions.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(3)"><i class='bx bx-left-arrow-alt'></i> Previous: Supply & Demand</button>
                    <button class="nav-btn primary" onclick="showModule(5)">Next: Entry Models <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

MODULE_5 = """            <!-- MODULE 5 -->
            <div class="module-content-pane" id="module-5">
                <div class="module-hero">
                    <span class="module-number">Execution Precision</span>
                    <h1>Module 5: SMC High-Probability Entry Models & Execution Mastery</h1>
                    <p>The 3 master entry blueprints, session kill zones, precision stop-loss engineering, and asymmetric trade management.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 62.5%;"></div>
                    </div>
                </div>

                <!-- 1. THE 3 MASTER ENTRY BLUEPRINTS -->
                <div class="content-section">
                    <h3><i class='bx bx-target-lock'></i> 1. The 3 Master Institutional Entry Blueprints</h3>
                    <p>An institutional Point of Interest (POI) is useless without a surgical entry trigger. Smart Money Concepts utilizes three mechanical entry blueprints, trading off execution certainty against risk-to-reward ratio.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">Blueprint 1: The Risk Entry (Direct Limit)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Setting a resting limit order directly on an unmitigated HTF Order Block or FVG proximal line. Stop loss is placed outside the distal edge.</p>
                            <p style="font-size: 12px; color: var(--vip-text-muted); margin-top: 6px;"><strong>Pros:</strong> Guarantees fills on rapid touches; zero FOMO.<br><strong>Cons:</strong> Lower win rate (60%); vulnerable to deep liquidity sweeps.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Blueprint 2: The Confirmation Entry (Sniper)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Wait for HTF POI to be tapped. Drop to LTF (M5 / M1). Await a local liquidity sweep followed by an explosive CHoCH + FVG. Enter on the retest of the LTF FVG.</p>
                            <p style="font-size: 12px; color: #00ff88; margin-top: 6px;"><strong>Pros:</strong> Highest win rate (75%-82%); ultra-tight stops; 1:6 to 1:15 R:R.<br><strong>Cons:</strong> Can occasionally leave without you on high-velocity news moves.</p>
                        </div>
                    </div>
                </div>

                <!-- 2. SVG BLUEPRINT SCHEMATIC -->
                <div class="content-section">
                    <h3><i class='bx bx-sitemap'></i> 2. Anatomy of the Precision Confirmation Entry</h3>
                    <p>The multi-timeframe confirmation process step-by-step from HTF macro context down to the 1-minute execution trigger.</p>

                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 340" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- HTF POI Box -->
                                <rect x="30" y="220" width="340" height="90" fill="rgba(0, 255, 136, 0.12)" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="4,4" rx="6" />
                                <text x="180" y="270" fill="#00ff88" font-size="13" font-weight="800" text-anchor="middle">H4 / H1 UNMITIGATED DEMAND POI</text>

                                <!-- Price Approach Curve (LTF) -->
                                <polyline points="50,60 110,180 150,130 210,235 240,190 280,270" fill="none" stroke="#ff4444" stroke-width="2" />
                                <text x="200" y="110" fill="#aaa" font-size="10">Approach into HTF POI</text>

                                <!-- Liquidity Sweep inside POI -->
                                <circle cx="280" cy="270" r="7" fill="rgba(255, 68, 68, 0.4)" stroke="#ff4444" stroke-width="2" />
                                <text x="280" y="295" fill="#ff4444" font-size="10" font-weight="800" text-anchor="middle">1. SWEEPS M5 LOW</text>

                                <!-- Violent Displacement Upside -->
                                <path d="M 280 270 L 380 90 L 440 160 L 620 40 L 740 50" fill="none" stroke="#00ff88" stroke-width="3" />

                                <!-- CHoCH Line -->
                                <line x1="240" y1="190" x2="420" y2="190" stroke="var(--vip-gold)" stroke-width="1.5" stroke-dasharray="3,3" />
                                <text x="340" y="180" fill="var(--vip-gold)" font-size="11" font-weight="800">2. M5 / M1 CHoCH</text>

                                <!-- FVG Retest Box -->
                                <rect x="410" y="150" width="55" height="40" fill="rgba(214, 255, 0, 0.25)" stroke="var(--vip-gold)" stroke-width="1.5" rx="3" />
                                <text x="437" y="210" fill="var(--vip-gold)" font-size="10" font-weight="800" text-anchor="middle">3. RETEST FVG</text>
                                <text x="437" y="224" fill="#fff" font-size="9" text-anchor="middle">SNIPER ENTRY</text>

                                <!-- Target Pool -->
                                <line x1="380" y1="40" x2="740" y2="40" stroke="#00ff88" stroke-width="1" stroke-dasharray="3,3" />
                                <text x="680" y="30" fill="#00ff88" font-size="11" font-weight="700">4. TARGET: HTF BSL (1:8 R:R)</text>

                                <!-- Stop Loss Marker -->
                                <line x1="410" y1="280" x2="490" y2="280" stroke="#ff4444" stroke-width="2" />
                                <text x="450" y="295" fill="#ff4444" font-size="9" font-weight="700" text-anchor="middle">STOP LOSS (Below Origin)</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The Confirmation Entry Blueprint: HTF Demand tap -> M1/M5 liquidity purge -> Aggressive displacement breaking structure (CHoCH) -> Limit entry on LTF FVG retest -> Stop placed safely below swing origin.</p>
                    </div>
                </div>

                <!-- 3. SESSION KILL ZONES & TIMING -->
                <div class="content-section">
                    <h3><i class='bx bx-time-five'></i> 3. Session Kill Zones: Timing the Algorithmic Injection</h3>
                    <p>Institutions do not execute random trades throughout the day. Institutional volume injections occur during precise algorithmic time windows called <strong>Session Kill Zones</strong>. If a setup occurs outside these hours, the probability drops by over 50%.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Session Kill Zone</th>
                                    <th>GMT / UTC Time</th>
                                    <th>EST / New York Time</th>
                                    <th>Algorithmic Behavior</th>
                                    <th>Key Asset Classes</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Asian Range</strong></td>
                                    <td>00:00 - 06:00 GMT</td>
                                    <td>19:00 - 01:00 EST</td>
                                    <td>Tight consolidation; builds initial BSL & SSL</td>
                                    <td>AUD, NZD, JPY crosses</td>
                                </tr>
                                <tr>
                                    <td><strong>London Open Kill Zone</strong></td>
                                    <td>07:00 - 10:00 GMT</td>
                                    <td>02:00 - 05:00 EST</td>
                                    <td>Judas Swing manipulation; sets daily High/Low</td>
                                    <td>GBP/USD, EUR/USD, XAU/USD</td>
                                </tr>
                                <tr>
                                    <td><strong>New York AM Kill Zone</strong></td>
                                    <td>12:00 - 15:00 GMT</td>
                                    <td>07:00 - 10:00 EST</td>
                                    <td>High-impact news overlap; trend continuation/reversal</td>
                                    <td>EUR/USD, US30, NAS100, Gold</td>
                                </tr>
                                <tr>
                                    <td><strong>London Close Kill Zone</strong></td>
                                    <td>15:00 - 17:00 GMT</td>
                                    <td>10:00 - 12:00 EST</td>
                                    <td>Institutional profit taking & counter-trend pullbacks</td>
                                    <td>All majors & indices</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4. TRADE MANAGEMENT & BREAKEVEN PROTOCOLS -->
                <div class="content-section">
                    <h3><i class='bx bx-shield-quarter'></i> 4. Precision Trade Management & Breakeven Protocols</h3>
                    <p>Entering a trade is only 20% of the game; trade management determines your long-term equity growth. Amateur traders move stops to breakeven too early or let winning trades retrace into losses.</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num">1</div>
                            <strong style="color: var(--vip-gold); font-size: 14px;">The 2R Invalidation Barrier:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never move stop loss to breakeven until price has achieved at least <strong>2R profit AND created a new M15 Break of Structure (BOS)</strong> in your favor.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">2</div>
                            <strong style="color: #00ff88; font-size: 14px;">The Partial Harvest Rule (80/20):</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Close 50% of your position at 1:3 R:R to lock in capital profit. Allow the remaining 50% runner to target HTF liquidity with stops protected at Breakeven.</p>
                        </div>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: SMC Entry Confluence Scorer</h3>
                    <p>Calculate your entry clearance score before pulling the trigger. Ensure your setup satisfies all institutional confluence parameters.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-target-lock'></i> Execution Confluence Calculator</h4>
                            <span class="badge-institutional">MODULE 5 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-time'></i> Session Kill Zone Timing</label>
                                <select id="m5KillZone">
                                    <option value="25">London Open / NY AM Active Kill Zone (+25 Pts)</option>
                                    <option value="10">London Close Session (+10 Pts)</option>
                                    <option value="0">Dead Asian Mid-Day / Off Hours (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-layer'></i> Higher Timeframe POI Alignment</label>
                                <select id="m5HtfPoi">
                                    <option value="25">Tapped Unmitigated Daily/H4 Order Block or FVG (+25 Pts)</option>
                                    <option value="15">Tapped H1 POI Only (+15 Pts)</option>
                                    <option value="0">No HTF POI (Floating in Mid-Range) (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-git-branch'></i> Lower Timeframe Confirmation (M5/M1)</label>
                                <select id="m5LtfConfirm">
                                    <option value="30">Liquidity Sweep + Clean CHoCH + FVG Retest (+30 Pts)</option>
                                    <option value="15">BOS Only Without Liquidity Sweep (+15 Pts)</option>
                                    <option value="0">Direct Risk Limit Order with No Confirmation (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-slider'></i> Risk-to-Reward Ratio (R:R)</label>
                                <select id="m5RR">
                                    <option value="20">1:5 or Higher to Clear Opposing Liquidity (+20 Pts)</option>
                                    <option value="10">1:3 to 1:4 R:R (+10 Pts)</option>
                                    <option value="0">Under 1:2 R:R (Sub-Optimal) (0 Pts)</option>
                                </select>
                            </div>
                        </div>

                        <button class="calc-btn" onclick="scoreSMCEntry()" style="margin-top: 15px;">
                            <i class='bx bx-play'></i> Evaluate Entry Clearance Score
                        </button>

                        <div id="m5ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">EXECUTION CLEARANCE AUDIT</div>
                                <div id="m5GradeBadge" class="badge-aaa">GREEN LIGHT: SNIPER EXECUTION</div>
                            </div>
                            <div class="value" id="m5ScoreValue" style="text-align: center; font-size: 38px; margin: 15px 0;">100 / 100</div>
                            <p id="m5Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m5Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The 60-Second Pre-Flight Execution Checklist</h3>
                    <p>Tick off every condition before clicking Buy or Sell:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Kill Zone Clock Check:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Are you inside London Open (07:00-10:00 GMT) or NY AM (12:00-15:00 GMT)? If not, close the terminal.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">HTF POI Must Be Tapped:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Has price tapped an unmitigated Daily, H4, or H1 Order Block or FVG? Never trade mid-range chop.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Local Liquidity Swept:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Did the lower timeframe sweep a recent high or low before shifting structure?</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Clean Displacement & FVG:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Did the CHoCH break structure with full-bodied ERC candles and leave behind a clean Fair Value Gap?</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Stop Loss Positioned Outside Distal:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Is your stop loss placed 2-3 pips outside the structural origin swing wick to protect against spread spikes?</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Minimum 1:3 R:R Target:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Is your target resting at an opposing external liquidity pool offering at least 3 times your risk?</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Fixed 1% Position Sizing:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Did you use the Pro Toolbox lot size calculator to ensure exactly 1% account risk is allocated?</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 5 Masterclass: SMC Entry Models & Execution Mastery</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/5T3Y6_G8h1I?rel=0&modestbranding=1"
                            title="SMC Entry Models & Execution Mastery Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 22:15:</strong> The Confirmation CHoCH + FVG Retest Blueprint.</li>
                            <li><strong>22:16 - 38:40:</strong> Session Kill Zones: Exploiting London Judas Swings & NY Open.</li>
                            <li><strong>38:41 - 56:20:</strong> Stop Loss Engineering, Breakeven Protocols & Partial Scaling.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(4)"><i class='bx bx-left-arrow-alt'></i> Previous: Liquidity & OBs</button>
                    <button class="nav-btn primary" onclick="showModule(6)">Next: Fundamentals <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

print("Module 4 and Module 5 compiled.")
